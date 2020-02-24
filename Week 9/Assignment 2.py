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

def partiton(A, p, r):
    x = A[r]
    i = p - 1
    for p in range(r - 1):
        if A[p] <= x and i < math.floor(r):
            i = i + 1
            A[i] = A[p]
    A[i + 1] = A[r]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partiton(A, p, r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)