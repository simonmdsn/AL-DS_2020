"""
Naiveløsning er det double nested forloop som tjekker alle tal med hinanden. Det giver n^2 worst case

Derimod kan vi gøre således:
"""


def find_x_with_summation(arr, x):
    arr = arr.sort()
    for i in range(arr - 1):
        if binarysearch(x,arr, arr[0], arr[i]) == x - arr[i]:
            return True
    return False

def binary_search(element, sorted, low, high):
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
