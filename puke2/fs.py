# -*- coding: utf-8 -*-
import os
import time
import pwd
import grp
import shutil
import hashlib
from . import exceptions
from .settings.fs import RM_SECURITY

MD5 = "md5"
SHA1 = "sha1"


def HandleOsError(func, *args, **kwargs):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OSError as exc:
            if exc.errno in (1, 13):
                raise exceptions.PermissionDenied(args)
            else:
                raise exc

    return wrapper


class FileList(object):
    pass


def find():
    raise NotImplemented()


@HandleOsError
def mkdir(path):
    if exists(path) and isdir(path):
        return True

    if exists(path):
        raise exceptions.FileExists(path)

    os.makedirs(path)


@HandleOsError
def copyfile():
    raise NotImplemented()


@HandleOsError
def readfile():
    raise NotImplemented()


@HandleOsError
def writefile():
    raise NotImplemented()


@HandleOsError
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


@HandleOsError
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

    if isfile(path) or islink(path):
        os.remove(path)
    else:
        shutil.rmtree(path)


@HandleOsError
def checksum(path, algo=MD5):
    if not exists(path):
        raise exceptions.PathNotFound(path)

    path = realpath(path)

    if algo == SHA1:
        hashalgo = hashlib.sha1()
    elif algo == MD5:
        hashalgo = hashlib.md5()
    else:
        raise NotImplemented()

    data = None
    fh = None
    block_size = 2**20
    fh = open(path, 'rb')

    while True:
        data = fh.read(block_size)
        if not data:
            break
        hashalgo.update(data)

    fh.close()

    return hashalgo.hexdigest()


@HandleOsError
def exists(path):
    return os.path.exists(resolvepath(path))


@HandleOsError
def isfile(path, followSymlink=False):
    if not exists(path):
        raise exceptions.FileNotFound(path)

    if not followSymlink and islink(path):
        return False

    return os.path.isfile(resolvepath(path))


@HandleOsError
def isdir(path, followSymlink=False):
    if not exists(path):
        raise exceptions.DirectoryNotFound(path)

    if not followSymlink and islink(path):
        return False

    return os.path.isdir(resolvepath(path))


@HandleOsError
def islink(path):
    if not exists(path):
        raise exceptions.SymlinkNotFound(path)

    return os.path.islink(resolvepath(path))


@HandleOsError
def chown(path, uname=None, gname=None):
    path = resolvepath(path)

    if not uname:
        uid = os.stat(path).st_uid

    if not gname:
        gid = os.stat(path).st_gid

    if not isinstance(uname, int) and uname is not None:
        uid = getUid(uname)

    if not isinstance(gname, int) and gname is not None:
        gid = getGid(gname)

    if uid is None:
        raise exceptions.IllegalUserName(uname)

    if gid is None:
        raise exceptions.IllegalGroupName(gname)

    os.chown(path, uid, gid)


@HandleOsError
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


def getUid(name):
    try:
        return pwd.getpwnam(name)[2]
    except:
        return None


def getGid(name):
    try:
        return grp.getgrnam(name)[2]
    except:
        return None
