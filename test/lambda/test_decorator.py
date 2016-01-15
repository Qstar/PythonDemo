import functools
import time


def performance(unit):
    def fn(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return f(*args, **kw)

        return wrapper

    return fn


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial.__name__
# print factorial(5)
