"""
    Implementer Mergesort ud fra bogens pseudokode. Side 31.
    Kør eksekveringstest på dem.
"""

import time
import random
from cmath import inf


def makeListFromNumberOfParameters(n, shuffle, reverse):
    listen = []
    for i in range(n - 1):
        listen.append(i)
    if reverse:
        listen.reverse()
    if shuffle:
        random.shuffle(listen)
    return listen


def merge(elements, low, high, right):
    left = elements(range(low, high - 1))
    right = elements(range(high, len(elements) - 1))
    left.append(inf)
    right.append(inf)

