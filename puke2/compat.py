# -*- coding: utf-8 -*-

# compat 2.6
try:
    from inspect import getcallargs
except:
    def getcallargs(*args):
        pass
