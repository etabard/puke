# -*- coding: utf-8 -*-


class PukeException(RuntimeError):
    pass


class TaskNotFound(PukeException):
    pass


class PukefileNotFound(PukeException):
    pass
