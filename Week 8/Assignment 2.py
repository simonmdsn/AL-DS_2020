"""
Eksamen juni 2011, opgave 2.

Lad f1, f2, g1 og g2 være positive funktioner, som opfylder, at
f1(n)∈ O(g1(n))
f2(n)∈ O(g2(n))

Hvilke af følgende tre udsagn er da sande?
"""

"""
(a) f1(n) + f2(n) ∈ O(g1(n) + g2(n))

Dette vil være sand, da summen af 2 øvre grænser altid vil være større.

"""

"""
(b) g1(n) + g2(n) ∈ Ω(f1(n) + f2(n))

Da opgaven beskriver, at f1(n)∈ O(g1(n)) og f2(n)∈ O(g2(n)), kan vi anvende omskrivningen f(n) = O(g(n)) <-> g(n) = Ω(f(n))

Altså må den være sand.
"""

"""
(c) ( f1(n) / f2(n) ) ∈ O ( g1(n) / g2(n) )

Falsk. Modeksempel: f1(n^3), f2(n^2), g1(n^2), g2(n). n er ikke en øvre grænse for n.
"""

