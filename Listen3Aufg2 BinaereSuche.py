import random
liste = [0]*20
for i in range(len(liste)):
    liste[i] = random.randint(1,49); 
print("listen erstellung erfolgreich")

liste.sort();print(liste)   #liste.sort => sortiert die liste aufsteigend

def binäreSuche(zahl):      #erstellt eine funktion
    a = 0
    b = len(liste)-1
    m = (b+a) // 2  #//keine kommazahlen ; m = mitte der liste

    while liste[m] != zahl and b > a: #solange index m(hälfte) nicht = gesuchte zahl und listenlänge größer a
        if liste[m] > zahl:                     #wenn eintrag der mitte der liste > zahl, dann      
            b = m+1                   #b wird zur hälfte +1
        else:                                   
            a = m-1                             
        m=(b+a) // 2                  
    if liste[m] == zahl:
        return m ; 
    else:
        return -1 ; 

print(binäreSuche(19))







"""


liste = [1, 3, 5, 7, 9, 11, 13]
         0  1  2  3  4   5   6

1. Durchlauf:

    a = 0
    liste_länge = 6
    m = (6 + 0) // 2 = 3
    liste[3] = 7
    7 < 9 → wir müssen rechts weitersuchen
    a = 3 + 1 = 4

2. Durchlauf:

    a = 4
    liste_länge = 6
    m = (6 + 4) // 2 = 5
    liste[5] = 11
    11 > 9 → wir müssen links weitersuchen
    liste_länge = 5 - 1 = 4

3. Durchlauf:

    a = 4
    liste_länge = 4
    m = (4 + 4) // 2 = 4
    liste[4] = 9
    9 == 9 → gefunden
    return 4
"""