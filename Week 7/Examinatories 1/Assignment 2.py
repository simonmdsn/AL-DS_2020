"""
Cormen et al. øvelse 2.2-3 (side 29). Svar ogs̊a for best-case køretid.

Consider linear search again (see Exercise 2.1-3).
How many elements of the input sequence need to be checked on the average,
assuming that the element being searched for is equally likely to be any element in the array?
How about in the in worst case?
What are the average-case and worst-case running times of linear search in Θ-notation?
Justify your answers.


"""

"""
    Hvis sekvensen er oprigtig tilfældig vil halvdelen af elementerne skulle checkes, da man kan forvente, at elementet optræder i midten af sekvensen i gennemsnit.
    tj = t = tiden i forhold til antal elementer j
    Average: tj = 2 / j, hvor j er antallet af gennemløb af sekvensen.
    Worst: tj = j, elementet er sidst i sekvensen.
    Best: tj = 1, elementet er det første i sekvensen.
"""

