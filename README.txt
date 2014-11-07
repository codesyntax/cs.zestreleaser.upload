========================================
Custom egg upload where the user wants
========================================

This package provides a plugin for ``zest.releaser`` that offers to upload the
released egg via SCP, SFTP or HTTP(S) PUT (WebDAV) to a custom location (instead of or
in addition to PyPI).

This plugin is based on `gocept.zestreleaser.customupload`_ to do the upload process
and uses the `distbase` and `distdefault` concept of `jarn.mkrelease`_, so you need to
add something like this to your ``~/.pypirc`` like the following::

    [cs.zestreleaser.upload]
    _default_with_input_ = scp://download.gocept.com//var/www/customers/
    _default_ = scp://download.gocept.com//var/www/packages


If the option ``_default_with_input`` is set, the script will ask the user a folder name
that will be appended to the setting, and the created egg will be uploaded there and the
script will finish there.

This option is useful if you have a folder where you have one folder per project/customer
in the same place.

If the option ``_default_with_input`` is not set and ``_default_`` is set, the script will
upload the egg to that destination. This is usefull as a default destination of your eggs.


Options for HTTP(S) PUT (WebDAV)
================================

This option is the same as in `gocept.zestreleaser.customupload`_ so
HTTP(S) PUT (WebDAV) is implemented using `curl` to add options to `curl`,
e. g. to disable certificate checks, add the options in front of the URL
like this::

    [cs.zestreleaser.upload]
    gocept.special = --insecure https://dav.gocept.com/special



Development
===========

The source code is available in the git repository at
https://github.com/codesyntax/cs.zestreleaser.upload

Please report any bugs you find at
https://github.com/codesyntax/cs.zestreleaser.upload/issues

.. _`jarn.mkrelease`: https://pypi.python.org/pypi/jarn.mkrelease
.. _`gocept.zestreleaser.customupload`: https://pypi.python.org/pypi/gocept.zestreleaser.customupload

