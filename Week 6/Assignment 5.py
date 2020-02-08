"""
    Hvis et array/ en liste indeholder en permutation af tallene 0 til n-1 kan man
    definere kredse på samme måde som for puslespillet fra første forelæsning:
    et tal x, som står på plads y i arrayet, giver en pil fra plads y til plads x (dvs.
    hvis tallet 1 står på plads 4 i arrayet, er der en pil fra plads 4 til plads 1),
    og en samling pile, der hænger sammen i en cyklisk kæde, kaldes en kreds

    Lav en alogritme, som tæller antal kredse i en permutation.
    Hvad er køretiden for din alogirme som funktion af n?
"""

import random


def listorshuffledlist(n, shuffle):
    list = []
    for i in range(n):
        list.append(i)
    if shuffle:
        random.shuffle(list)
    return list


def findcycles(index, shuffled):
    print("List:", shuffled)
    cycles = 0
    while len(index) > 0:
        s = index[0]
        index.remove(s)
        currentIndex = s
        nextindex = shuffled[currentIndex]
        while currentIndex != nextindex:
            index.remove(nextindex)
            nextindex = shuffled[nextindex]
        cycles += 1
    return cycles


numbers = listorshuffledlist(8, False)
shuffled = listorshuffledlist(8, True)
print("Number of cycles:", findcycles(numbers, shuffled))
