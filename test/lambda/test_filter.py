import math


def is_sqr(x):
    if len(str(math.sqrt(x)).strip('.0')) == 1:
        return x


print filter(is_sqr, range(1, 101))
