from setuptools import setup, find_packages
import os

version = '1.0'

setup(
    name='cs.zestreleaser.upload',
    version=version,
    description="zest.releaser plugin to enter from the command-line the destination of the upload",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
        ],
    keywords='',
    author='Mikel Larreategi',
    author_email='mlarreategi@codesyntax.com',
    url='https://github.com/codesyntax/cs.zestreleaser.upload',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['cs', 'cs.zestreleaser'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zest.releaser',
    ],
    entry_points={
        'zest.releaser.releaser.after':
            ['csupload=cs.zestreleaser.upload.upload:upload',
            ]},
      )
