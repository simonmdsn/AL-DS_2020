"""
Cormen et al. øvelse 7.1-2 (side 174
"""

"""
What value of q does PARTITION return when all elements in the array[p..r] have the same value? 
Modify PARTITION so that q = [(p + r / 2)] when all elements in the array A[p..r} have the same value.
"""

"""
1) The value of q is r.

2)
"""
import math

def partition(A, p, r):
    x = A[r]
    i = p - 1
    c = 0
    for p in range(r - 1):
        if A[p] < x:
            i = i + 1
            A[i] = A[p]
        elif A[j] == x:
            if c%2 == 0:
                i = i + 1
                A[i] = A[j]
    A[i + 1] = A[r]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
