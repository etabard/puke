# -*- coding: utf-8 -*-
import os
import time
import pwd
import grp
import shutil
import hashlib


class FileList(object):
    pass


def find():
    pass


def mkdir():
    pass


def copyfile():
    pass


def readfile():
    pass


def writefile():
    pass


def rm():
    pass


def checksum():
    pass


def exists():
    pass


def isfile():
    pass


def isdir():
    pass


def chown():
    pass


def chmod():
    pass


def join(*args):
    return os.path.join(*args)


def abspath(path):
    return os.path.abspath(path)


def basename(path):
    return os.path.basename(path)


def dirname(path):
    return os.path.dirname(path)


def normpath(path):
    return os.path.normpath(path)


def sep():
    return os.sep


def realpath(path):
    return os.path.realpath(os.path.expanduser(path))
