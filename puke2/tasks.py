# -*- coding: utf8 -*-

import types
from inspect import getdoc
from .compat import getcallargs

from .exceptions import TaskNotFound
__tasks__ = {}


def add(task):
    __tasks__[task.name] = task


def hasDefault():
    return True if 'default' in __tasks__ else False


def execute(name, *args, **kwargs):
    if not name in __tasks__:
        raise TaskNotFound(name)

    __tasks__[name](*args, **kwargs)


def help(name):
    if not name in __tasks__:
        raise TaskNotFound(name)

    return getdoc(__tasks__[name].getFunc())


def list():
    result = ()
    for name in __tasks__:
        obj = __tasks__[name]
        result.append((name, obj.desc if obj.desc else None))

    return result


class Task:
    __doc__ = ""

    def __init__(self, func, desc=""):
        name = func.__name__
        self.__func = func

        self.name = name
        self.desc = desc
        self.fullname = "%s.%s" % (func.__module__, name)

        try:
            self.__doc__ = func.__doc__
        except AttributeError:
            pass

        add(self)

    def __call__(self, *args, **kw):
        try:
            getcallargs(self.__func, *args)
        except TypeError as e:
            help(self.name)
            raise

        retval = self.__func(*args)
        return retval

    def __repr__(self):
        return "puke.tasks.Task: " + self.name

    def getFunc(self):
        return self.__func


def task(func):
    """ Specifies that this function is a task. """

    if isinstance(func, Task):
        return func

    elif isinstance(func, types.FunctionType):
        return Task(func)

    else:
        # Used for descriptions
        def wrapper(finalfunc):
            return Task(finalfunc, func)

        return wrapper
