# -*- coding: utf-8 -*-

try:
    from inspect import getcallargs
except:
    def getcallargs(*args):
        pass
