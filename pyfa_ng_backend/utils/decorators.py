

import functools


def cache_control(max_age=300):
    def decorator(target):
        @functools.wraps(target)
        def wrapper(*args, **kwargs):
            response = target(*args, **kwargs)
            response = response + ({'Cache-Control': 'max-age={}'.format(max_age)}, )

            return response
        return wrapper
    return decorator
