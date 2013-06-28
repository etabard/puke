# -*- coding: utf-8 -*-


class PukeException(RuntimeError):
    pass


class TaskNotFound(PukeException):
    pass


class PukefileNotFound(PukeException):
    pass


class PathNotFound(PukeException):
    pass


class FileNotFound(PathNotFound):
    pass


class DirectoryNotFound(PathNotFound):
    pass


class SymlinkNotFound(PathNotFound):
    pass


class FileExists(PukeException):
    pass
