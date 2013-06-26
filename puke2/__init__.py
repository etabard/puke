# -*- coding: utf-8 -*-

__title__ = 'puke2'
__version__ = '2.0.0'
__build__ = hex(1)
__author__ = 'Emmanuel Tabard'
__license__ = 'MIT'
__copyright__ = 'Copyright 2011-2013 Web It Up, Emmanuel Tabard'

from . import http
from . import cache
from . import system
from . import utils
from . import fs
from . import log
from . import exceptions
from . import js
from . import css
from . import tools
from . import experimental
from . import display
from . import logging
from . import tasks
from .dependencies import sh


cache.internal = cache.FileSystemCache()


def run():
    from optparse import OptionParser
    import sys

    parser = OptionParser()
    parser.add_option("-c", "--clear", action="store_true", dest="clearcache", help="Spring time, clean all the vomit")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose", help="don't print status messages to stdout")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="print more detailed status messages to stdout")
    parser.add_option("-t", "--tasks",action="store_true",  dest="list_tasks", help="list tasks")
    parser.add_option("-l", "--log", dest="logfile", help="Write debug messages to given logfile")
    parser.add_option("-f", "--file", dest="file", help="Use the given build script")
    parser.add_option("-i", "--info",action="store_true",  dest="info", help="puke task --info show task informations")
    parser.add_option("-V", "--version",action="store_true",  dest="version", help="print the Puke version")
    
    if sys.platform.lower() == "darwin":
        parser.add_option("-s", "--speak",action="store_true",  dest="speak", help="puke speaks on fail/success")

    (options, args) = parser.parse_args()


    #output version
    if options.version:
        print("Puke %s" % __version__)

def main():
    import sys
    
    try:
        run()
    except Exception as error:
        print("Exception", error)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Build interrupted")
        sys.exit(2)

    sys.exit(0)
