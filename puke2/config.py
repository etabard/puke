# -*- coding: utf-8 -*-

import json
from . import fs
import copy


def load(path):
    payload = None
    if isinstance(path, (list, dict, tuple)):
        payload = path
        return File(payload)

    try:
        payload = json.loads(path)
        return File(payload)
    except:
        pass

    if fs.exists(path) and not fs.isdir(path):
        try:
            payload = fs.readfile(path)
            return File(payload)
        except:
            pass
    raise Exception("bad file")


class File(object):
    raw = {}
    content = {}

    def __init__(self, payload):
        self.raw = payload
        self.update()

    def update(self):
        self.content = copy.deepcopy(self.raw)
        self._compute(self.content)

    def _compute(self, data):

        if isinstance(data, list):
            dataIter = enumerate(data)
        elif isinstance(data, dict):
            dataIter = data.items()
        else:
            return

        for (node, value) in dataIter:
            print("======>", node, value)
            if isinstance(value, (str, unicode)):
                value += "$$$"
                data[node] = value
                continue
            elif isinstance(value, int):
                continue
            else:
                self._compute(value)


class DotDictify(dict):
    def __init__(self, value=None):
        if value is None:
            pass
        elif isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])
        else:
            raise TypeError('expected dict')

    def __setitem__(self, key, value):
        if '.' in key:
            myKey, restOfKey = key.split('.', 1)
            target = self.setdefault(myKey, DotDictify())
            if not isinstance(target, DotDictify):
                raise KeyError(
                    'cannot set "%s" in "%s" (%s)'
                    % (restOfKey, myKey, repr(target))
                )
            target[restOfKey] = value
        else:
            if isinstance(value, dict) and not isinstance(value, DotDictify):
                value = DotDictify(value)
            dict.__setitem__(self, key, value)

    def __getitem__(self, key, default=None):
        if '.' not in key:
            return dict.__getitem__(self, key)
        myKey, restOfKey = key.split('.', 1)
        target = dict.__getitem__(self, myKey)
        if not isinstance(target, DotDictify):
            raise KeyError(
                'cannot get "%s" in "%s" (%s)'
                % (restOfKey, myKey, repr(target))
            )
        return target.__getitem__(restOfKey) or default

    def __contains__(self, key):
        if '.' not in key:
            return dict.__contains__(self, key)
        myKey, restOfKey = key.split('.', 1)
        target = dict.__getitem__(self, myKey)
        if not isinstance(target, DotDictify):
            return False
        return restOfKey in target

    def setdefault(self, key, default):
        if key not in self:
            self[key] = default
        return self[key]

    __setattr__ = __setitem__
    __getattr__ = __getitem__
    get = __getattr__
