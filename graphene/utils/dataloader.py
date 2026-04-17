from asyncio import (
    gather,
    ensure_future,
    get_event_loop,
    iscoroutine,
    iscoroutinefunction,
)
from collections import namedtuple
from collections.abc import Iterable
from functools import partial

from typing import List

Loader = namedtuple("Loader", "key,future")


def iscoroutinefunctionorpartial(fn):
    pass


class DataLoader(object):
    batch = True
    max_batch_size = None  # type: int
    cache = True

    def __init__(
        self,
        batch_load_fn=None,
        batch=None,
        max_batch_size=None,
        cache=None,
        get_cache_key=None,
        cache_map=None,
        loop=None,
    ):
        self._loop = loop

        if batch_load_fn is not None:
            self.batch_load_fn = batch_load_fn

        assert iscoroutinefunctionorpartial(
            self.batch_load_fn
        ), "batch_load_fn must be coroutine. Received: {}".format(self.batch_load_fn)

        if not callable(self.batch_load_fn):
            raise TypeError(  # pragma: no cover
                (
                    "DataLoader must be have a batch_load_fn which accepts "
                    "Iterable<key> and returns Future<Iterable<value>>, but got: {}."
                ).format(batch_load_fn)
            )

        if batch is not None:
            self.batch = batch  # pragma: no cover

        if max_batch_size is not None:
            self.max_batch_size = max_batch_size

        if cache is not None:
            self.cache = cache  # pragma: no cover

        self.get_cache_key = get_cache_key or (lambda x: x)

        self._cache = cache_map if cache_map is not None else {}
        self._queue: List[Loader] = []

    @property
    def loop(self):
        pass

    def load(self, key=None):
        """
        Loads a key, returning a `Future` for the value represented by that key.
        """
        pass

    def do_resolve_reject(self, key, future):
        # Enqueue this Future to be dispatched.
        pass

    def load_many(self, keys):
        """
        Loads multiple keys, returning a list of values

        >>> a, b = await my_loader.load_many([ 'a', 'b' ])

        This is equivalent to the more verbose:

        >>> a, b = await gather(
        >>>    my_loader.load('a'),
        >>>    my_loader.load('b')
        >>> )
        """
        pass

    def clear(self, key):
        """
        Clears the value at `key` from the cache, if it exists. Returns itself for
        method chaining.
        """
        pass

    def clear_all(self):
        """
        Clears the entire cache. To be used when some event results in unknown
        invalidations across this particular `DataLoader`. Returns itself for
        method chaining.
        """
        pass

    def prime(self, key, value):
        """
        Adds the provied key and value to the cache. If the key already exists, no
        change is made. Returns itself for method chaining.
        """
        pass


def enqueue_post_future_job(loop, loader):
    pass


def get_chunks(iterable_obj, chunk_size=1):
    pass


def dispatch_queue(loader):
    """
    Given the current state of a Loader instance, perform a batch load
    from its current queue.
    """
    pass


async def dispatch_queue_batch(loader, queue):
    # Collect all keys to be loaded in this dispatch
    pass


def failed_dispatch(loader, queue, error):
    """
    Do not cache individual loads if the entire batch dispatch fails,
    but still reject each request so they do not hang.
    """
    pass
