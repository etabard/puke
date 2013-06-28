# -*- coding: utf-8 -*-
import os
import time
import pwd
import grp
import shutil
import hashlib
from . import exceptions
from .settings.fs import RM_SECURITY


class FileList(object):
    pass


def find():
    raise NotImplemented()


def mkdir(path):
    if exists(path) and isdir(path):
        return True

    if exists(path):
        raise exceptions.FileExists(path)

    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == 13:
            raise exceptions.PermissionDenied(path)
        else:
            raise exc


def copyfile():
    raise NotImplemented()


def readfile():
    raise NotImplemented()


def writefile():
    raise NotImplemented()


def symlink(source, symlink):
    if exists(symlink):
        raise exceptions.FileExists(symlink)

    if not exists(source):
        raise exceptions.PathNotFound(source)

    try:
        #dead symlink
        os.readlink(symlink)
        symlinkExists = True
    except OSError:
        symlinkExists = False

    if symlinkExists:
        os.remove(symlink)

    os.symlink(source, symlink)


def rm(path):
    path = abspath(resolvepath(path))

    if not exists(path):
        raise exceptions.PathNotFound(path)

    for checkpath in RM_SECURITY:
        if path == abspath(resolvepath(checkpath)):
            raise exceptions.SecurityError(
                "Cannot delete %s contained in security sandbox %s "
                % (path, RM_SECURITY)
            )

    try:
        if isfile(path) or islink(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
    except OSError as exc:
        if exc.errno == 13:
            raise exceptions.PermissionDenied(path)
        else:
            raise exc


def checksum():
    raise NotImplemented()


def exists(path):
    return os.path.exists(resolvepath(path))


def isfile(path, followSymlink=False):
    if not exists(path):
        raise exceptions.FileNotFound(path)

    if not followSymlink and islink(path):
        return False

    return os.path.isfile(resolvepath(path))


def isdir(path, followSymlink=False):
    if not exists(path):
        raise exceptions.DirectoryNotFound(path)

    if not followSymlink and islink(path):
        return False

    return os.path.isdir(resolvepath(path))


def islink(path):
    if not exists(path):
        raise exceptions.SymlinkNotFound(path)

    return os.path.islink(resolvepath(path))


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


def resolvepath(path):
    return os.path.expanduser(path)


def realpath(path):
    return os.path.realpath(resolvepath(path))
