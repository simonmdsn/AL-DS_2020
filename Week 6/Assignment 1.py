"""
1.  Cormen et al. problem 1.1 (side 14).
Erstat dog “microseconds” med“nanoseconds”  (dvs.  10^-9 sekunder), da  dette  ca.  er  hvad  en  CPU-cyklus tager på en moderne processor.
Du skal kun udfylde søjlerne second,day,century.
For nogle af indgangene kan man finde svaretved matematisk udregning, for andre må man prøve sig frem ved at¨indsætte forskellige værdier af n.
"""

"""
    lg n  for 1 sekund
    lg n = 1
    
    løser for n,
    n = 10^1
    n = 10
    
    Omregne til nanosekunder
    
    n = 10^9
    
    lg n for 1 dag
    1 dag = 86400 sekunder
    
    lg n = 86400
    n = 10^86400
    
    Omregne til nanosekunder
    n = (10^86400)^9
    
    lg n for et årti
    årti = 3,1556926 * 10^9 sekunder
    
    lg n = 3,1556926 * 10^9
    n = 10^3,1556926 * 10^9
    
    Omregne til nanosekunder
    
    n = (10^3,1556926 * 10^9)^9 = 2.51903e+109
"""