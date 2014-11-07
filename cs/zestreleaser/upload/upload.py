# This product reuses and redistributes code from Gocept
# with Copyright (c) 2010 gocept gmbh & co. kg
# According to the ZPL license of that code this copyright notice is retained
# Original repository of that code is at:
# https://code.gocept.com/hg/public/gocept.zestreleaser.customupload/

import ConfigParser
import glob
import logging
import os
import os.path
import urlparse
import zest.releaser.utils


def split_destination(destination):
    """Returns list of options and destination."""
    parts = destination.split()
    options = parts[:-1]
    destination = parts[-1]
    if '://' not in destination:
        destination = 'scp://' + destination.replace(':', '/', 1)
    return options, destination


def upload(context):
    if zest.releaser.utils.ask('Upload to client folder?', True):
        destination_folder = zest.releaser.utils.get_input('Enter folder/customer name: ')
        destination = get_default_destination(
            context['name'], read_configuration('~/.pypirc'),
            'cs.zestreleaser.upload') + destination_folder

        url = urlparse.urlsplit(split_destination(destination)[1])
        if url.password:
            url = url[0:1] + (url[1].replace(url.password, '<passwd>'),) + url[2:]
        target_url = urlparse.urlunsplit(url)
        if not zest.releaser.utils.ask('Upload to %s' % target_url):
            return
        sources = glob.glob(os.path.join(context['tagdir'], 'dist', '*'))
        for call in get_calls(sources, destination):
            os.system(' '.join(call))


def get_calls(sources, destination):
    result = []
    options, destination = split_destination(destination)
    url = urlparse.urlsplit(destination)
    if url[0] in ('scp', ''):
        netloc, path = url[1], url[2]
        assert path.startswith('/')
        path = path[1:]
        result.append(['scp'] + sources + ['%s:%s' % (netloc, path)])
    if url[0] in ('http', 'https'):
        if destination.endswith('/'):
            destination = destination[:-1]
        default_params = ['curl']
        default_params.extend(options)
        default_params.extend(['-X', 'PUT', '--data-binary'])
        default_params = tuple(default_params)
        for source in sources:
            source_name = os.path.basename(source)
            result.append(
                list(default_params +
                     ('@' + source, '%s/%s' % (destination, source_name))))
    if url[0] in ('sftp', ):
        netloc, path = url[1], url[2]
        assert path.startswith('/')
        for source in sources:
            result.append(
                ['echo', '"put %s"' % source, '|', 'sftp',
                    '-b', '-', "%s:%s" % (netloc, path)])
    return result


def read_configuration(filename):
    config = ConfigParser.ConfigParser()
    config.read(os.path.expanduser(filename))
    return config


# def choose_destination(package, config, section):
#     if section not in config.sections():
#         return None
#     items = sorted(config.items(section), key=lambda x: len(x[0]),
#                    reverse=True)
#     package = package.lower()
#     for prefix, destination in items:
#         if package.startswith(prefix.lower()):
#             return destination
#     return None


def get_default_destination(package, config, section):
    logger = logging.getLogger(__name__)
    if section not in config.sections():
        return None
    items = sorted(config.items(section), key=lambda x: len(x[0]),
                   reverse=True)
    package = package.lower()
    for prefix, destination in items:
        if package.startswith(prefix.lower()):
            return destination

    try:
        # Let's see if there's a default path that requires
        # input from the user
        default_with_input = config.get(section, '_default_with_input_')
        logger.debug('Default path with input: %s' % default_with_input)
        if not default_with_input.endswith('/'):
            default_with_input += '/'
        return default_with_input
    except ConfigParser.NoOptionError:
        # Let's see if there's a default path to rule them all
        logger.debug('No default path with input from user')

    try:
        default = config.get(section, '_default_')
        logger.debug('Default path: %s' % default)
        return default
    except ConfigParser.NoOptionError:
        # There is nothing here, return None
        return None

    return None
