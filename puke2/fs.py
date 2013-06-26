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
    raise NotImplemented()


def mkdir():
    raise NotImplemented()


def copyfile():
    raise NotImplemented()


def readfile():
    raise NotImplemented()


def writefile():
    raise NotImplemented()


def rm():
    raise NotImplemented()


def checksum():
    raise NotImplemented()


def exists():
    raise NotImplemented()


def isfile():
    raise NotImplemented()


def isdir():
    raise NotImplemented()


def chown():
    raise NotImplemented()


def chmod():
    raise NotImplemented()


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
