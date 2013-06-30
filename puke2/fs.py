# -*- coding: utf-8 -*-
import os
import time
import pwd
import grp
import shutil
import errno
import hashlib
from . import exceptions
from .settings.fs import RM_SECURITY
from .utils import octalmode

MD5 = "md5"
SHA1 = "sha1"


def HandleOsError(func, *args, **kwargs):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (OSError, IOError) as exc:
            message = abspath(exc.filename)
            # See http://docs.python.org/2/library/errno.html
            if exc.errno in (
                errno.EPERM,  # Operation not permitted
                errno.EACCES  # Permission denied
            ):
                raise exceptions.PermissionDenied(message)
            elif exc.errno == errno.ENOENT:
                raise exceptions.PathNotFound(message)
            elif exc.errno == errno.EISDIR:
                raise exceptions.UnexpectedDirectory(message)
            else:
                raise exc

    return wrapper


@HandleOsError
def mkdir(path):
    if not path.strip():
        return False

    if exists(path) and isdir(path):
        return True

    if exists(path):
        raise exceptions.FileExists(abspath(path))

    os.makedirs(path)


@HandleOsError
def copyfile(sourcepath, destpath, force=False):
    sourcepath = resolvepath(sourcepath)
    destpath = resolvepath(destpath)

    if not exists(sourcepath):
        raise exceptions.FileNotFound(abspath(sourcepath))

    if isdir(sourcepath):
        raise exceptions.UnexpectedDirectory(abspath(sourcepath))

    try:
        src_mtime = os.path.getmtime(sourcepath)
    except:
        src_mtime = 0

    try:
        dst_mtime = os.path.getmtime(destpath)
    except:
        dst_mtime = 0

    if not force and src_mtime == dst_mtime:
        return False

    shutil.copy2(sourcepath, destpath)

    return True


@HandleOsError
def readfile(path):
    path = resolvepath(path)
    data = None
    fh = None

    if not exists(path):
        raise exceptions.FileNotFound(abspath(path))

    if isdir(path):
        raise exceptions.UnexpectedDirectory(abspath(path))

    try:
        fh = open(path)
        data = fh.read()
    except (OSError, IOError) as exc:
        raise exc
    finally:
        if fh:
            fh.close()

    return data


@HandleOsError
def writefile(path, content, mtime=None, binary=False):
    path = resolvepath(path)

    mkdir(dirname(path))

    mode = 'wb' if binary else 'w'
    fh = None

    try:
        fh = open(path, mode)
        fh.write(content)
    except (OSError, IOError) as exc:
        raise exc
    finally:
        if fh:
            fh.close()

    if mtime:
        os.utime(path, (time.time(), mtime))


@HandleOsError
def symlink(source, symlink):
    if exists(symlink):
        raise exceptions.FileExists(abspath(symlink))

    if not exists(source):
        raise exceptions.PathNotFound(abspath(source))

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
        raise exceptions.PathNotFound(abspath(path))

    path = realpath(path)

    if algo == SHA1:
        hashalgo = hashlib.sha1()
    elif algo == MD5:
        hashalgo = hashlib.md5()
    else:
        raise NotImplementedError()

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
        raise exceptions.FileNotFound(abspath(path))

    if not followSymlink and islink(path):
        return False

    return os.path.isfile(resolvepath(path))


@HandleOsError
def isdir(path, followSymlink=False):
    if not exists(path):
        raise exceptions.DirectoryNotFound(abspath(path))

    if not followSymlink and islink(path):
        return False

    return os.path.isdir(resolvepath(path))


@HandleOsError
def islink(path):
    if not exists(path):
        raise exceptions.SymlinkNotFound(abspath(path))

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
def chmod(path, mode):
    path = resolvepath(path)

    if not isinstance(mode, int):
        mode = octalmode(path, mode)

    os.chmod(path, mode)


def join(*args):
    return os.path.join(*args)


def abspath(path):
    return os.path.abspath(resolvepath(path))


def basename(path):
    return os.path.basename(resolvepath(path))


def dirname(path):
    return os.path.dirname(resolvepath(path))


def normpath(path):
    return os.path.normpath(resolvepath(path))


def relpath(path):
    return os.path.relpath(resolvepath(path))


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