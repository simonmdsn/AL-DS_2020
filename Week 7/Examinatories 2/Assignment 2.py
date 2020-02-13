"""
Vis for f(n) = 0.1 * n**2 + 5 * n + 25,
at f(n) = Θ(n**2) og f(n) = o(n**3). Brug sætninger side 17.

(0.1 * n**2 + 5 * n + 25 ) / n**2
=
(0.1 + 5 / n + 25 / n**2) / 1
= n går mod uendelig
0,1 + 0 + 0
=
0,1

SANDT ifølge sætning 1

(0.1 * n**2 + 5 * n + 25 ) / n**3
=
0.1 / n + 5 / n**3 + 25 / n**3
= GÅR  mod uendelig
0 + 0 + 0

SANDT ifølge sætning 2
"""