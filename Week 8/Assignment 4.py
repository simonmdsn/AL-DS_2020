"""
    Implementer Mergesort ud fra bogens pseudokode. Side 31.
    Kør eksekveringstest på dem.
"""
import math
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
    n_2 = right - high

    L = [0] * n_1
    R = [0] * n_2

    for i in range(n_1):
        L[i] = elements[low + i]

    for j in range(n_2):
        R[j] = elements[high + 1 + j]

    i = 0
    j = 0

    for k in range(low, right + 1):
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


def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

elements = makeListFromNumberOfParameters(10,True,False)
print(merge_sort(elements,1,10))
