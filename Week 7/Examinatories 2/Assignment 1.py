from random import random


def insertion_sort(list):
    print("Insertion sort")
    print("Unsorted:", list)
    for i in range(len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key
    return list


def makeListFromNumberOfParameters(n, shuffle, reverse):
    listen = []
    for i in range(n - 1):
        listen.append(i)
    if reverse:
        listen.reverse()
    if shuffle:
        random.shuffle(listen)
    return listen


numbers = makeListFromNumberOfParameters(10)
