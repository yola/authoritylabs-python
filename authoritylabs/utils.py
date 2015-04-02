from time import time


class memoized_ttl(object):
    """Decorator that caches a function for a certain time period

    If called within the TTL and the same arguments, the cached value is
    returned,
    If called outside the TTL or a different value, a fresh value is returned.
    """
    def __init__(self, ttl=None):
        self.cache = {}
        self.ttl = ttl

    def __call__(self, f):
        def wrapped_f(*args):
            now = time()
            try:
                value, last_update = self.cache[args]
                if self.ttl and 0 < self.ttl < now - last_update:
                    raise AttributeError
                return value
            except (KeyError, AttributeError):
                value = f(*args)
                self.cache[args] = (value, now)
                return value
            except TypeError:
                # uncachable -- for instance, passing a list as an argument.
                return f(*args)
        return wrapped_f
