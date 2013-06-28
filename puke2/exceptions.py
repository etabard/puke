# -*- coding: utf-8 -*-


class PukeException(RuntimeError):
    pass


class TaskNotFound(PukeException):
    pass


class PukefileNotFound(PukeException):
    pass


#FileSystem
class FileSystemError(PukeException):
    pass


class PermissionDenied(FileSystemError):
    pass


class SecurityError(FileSystemError):
    pass


class PathNotFound(FileSystemError):
    pass


class FileNotFound(PathNotFound):
    pass


class DirectoryNotFound(PathNotFound):
    pass


class SymlinkNotFound(PathNotFound):
    pass


class FileExists(FileSystemError):
    pass


class DirectoryExists(FileSystemError):
    pass


class IllegalUserName(FileSystemError):
    pass


class IllegalGroupName(FileSystemError):
    pass
