#!/usr/bin/env python

import os
import sys

import puke2 as puke

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'puke2',
    'puke2.dependencies.requests'
]

requires = [
    'psutil'
]


print(find_packages())
setup(
    name=puke.__title__,
    version=puke.__version__,
    description='A straightforward and versatile build system written in python',
    long_description=open('README.md').read() + '\n\n' +
                     open('HISTORY.md').read(),
    author=puke.__author__,
    author_email='manu@webitup.fr',
    url='http://puke.webitup.fr',
    packages=packages,
    package_data={'': ['LICENSE'], 'puke2': ['*.pem']},
    package_dir={'puke2': 'puke2'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'puke2 = puke2:main',
        ]
    },
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Build Tools'

    ),
)