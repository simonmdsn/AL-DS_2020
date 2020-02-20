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
    n_1 = low - high + 1
    n_2 = low - high

    L = [0] * n_1
    R = [0] * n_2

    for i in range(n_1):
        L[i] = elements[low + i]

    for j in range(n_2):
        R[j] = elements[high + 1 + j]

    i = 0
    j = 0

    for k in range(low, high + 1):
        if i >= n_1:
            elements[k] = R[j]
            j += 1
        elif j >= n_2:
            elements[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            elements[k] = L[i]
            i += 1
        else:
            elements[k] = R[j]
            j += 1
