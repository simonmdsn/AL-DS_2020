"""
    Lav et python-program, som generer en tilfædldig permutation
    af heltallene fra 0 til n-1 (for et n som er en input parameter).
    I python kan man bruge lister samt funktionen shuffle fra modulet random.
    Udskriv tallene i din permuation
"""

import random


def makeListFromNumberOfParameters(n, shuffle):
    list = []
    for i in range(n - 1):
        list.append(i)
    return shuffle if random.shuffle(list) else list

def printList(list):
    print(list)


printList(makeListFromNumberOfParameters(10, True))
