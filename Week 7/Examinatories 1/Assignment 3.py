"""
 Cormen et al. øvelse 2.3-5 (side 39)
 Write pseudocode, either iterative or recursive, for binary search. Argue that the worst-case running time of binary search is Θ(lg(n))
"""

"""
    NB. binary search forventer et stigende sorteret array.
"""
import random


def binarysearch(element, sorted, low, high):
    if high >= low:
        mid = (low + high) // 2
        # Midterste element
        if sorted[mid] == element:
            return mid
        # Større end mid
        elif sorted[mid] < element:
            return binarysearch(element, sorted, mid + 1, high)
        # Mindre end mid
        else:
            return binarysearch(element, sorted, low, mid - 1)
    return -1


def listorshuffledlist(n, shuffle):
    list = []
    for i in range(n):
        list.append(i)
    if shuffle:
        random.shuffle(list)
    return list


def randomlist(n):
    sorted = []
    for i in range(n):
        sorted.append(random.randint(0, 50))
    sorted[3] = 15
    sorted.sort()
    return sorted


sorted = listorshuffledlist(10, False)
print(sorted)
print("Your number exists at index:", binarysearch(3, sorted, 0, len(sorted)))
sortedrandomint = randomlist(10)
print(sortedrandomint)
print("Your number exists at index:",
      binarysearch(15, sortedrandomint, 0, len(sortedrandomint)))

"""
Vi halverer arrayets størrelse hver iteration i.
Altså:
    n / 2**i
    
"""