# -*- coding: utf-8 -*-

from .dependencies import requests
from .dependencies.requests import exceptions
from .dependencies.requests.auth import (
    HTTPBasicAuth as Basic,
    HTTPDigestAuth as Digest
)
from .settings.http import ALLOWABLE_CACHING_CODES, DEFAULT_CACHE, TTL
from . import cache


class CacheableSession(requests.Session):
    CACHEABLE = DEFAULT_CACHE
    TTL = TTL

    def __init__(self):
        super(CacheableSession, self).__init__()

    def send(self, request, *args, **kwargs):
        response = None
        if CacheableSession.CACHEABLE:
            response = from_cache(request, *args, **kwargs)

        if not response:
            response = super(CacheableSession, self).send(
                request, *args, **kwargs
            )

        return response

session = CacheableSession()


def from_cache(request, *args, **kwargs):
    result = cache.internal.get(request.url)
    return result if result else False


def to_cache(r, *args, **kw):
    if not r.status_code in ALLOWABLE_CACHING_CODES:
        return r

    cache.internal.set(r.url, r, CacheableSession.TTL)
    return r


def get(url, **kwargs):
    CacheableSession.CACHEABLE = DEFAULT_CACHE
    CacheableSession.TTL = TTL

    if 'cache' in kwargs:
        CacheableSession.CACHEABLE = kwargs['cache']
        kwargs.pop('cache', None)

    if 'ttl' in kwargs:
        CacheableSession.TTL = kwargs['ttl']
        kwargs.pop('ttl', None)

    if CacheableSession.CACHEABLE:
        kwargs['hooks'] = dict(response=to_cache)

    return session.get(url, **kwargs)


def options(url, **kwargs):
    return requests.options(url, **kwargs)


def head(url, **kwargs):
    return requests.head(url, **kwargs)


def post(url, data=None, **kwargs):
    return requests.post(url, data=data, **kwargs)


def put(url, data=None, **kwargs):
    return requests.put(url, data=data, **kwargs)


def patch(url, data=None, **kwargs):
    return requests.patch(url, data=data, **kwargs)


def delete(url, **kwargs):
    return requests.delete(url, **kwargs)
