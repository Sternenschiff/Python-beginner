from random import *

liste = [1]*6
for p in range(100):
    for i in range(len(liste)):
        x = randint(1,49)
        for n in range(len(liste)):
            if (liste[n] == x):
                i = i-1
        liste[i] = x
    print(liste)
    
    
