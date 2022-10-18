from functools import cache
import numpy as np

__all__ = ["my_sum", "factorial", 'sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


def sin(x):
    return np.sin(x)