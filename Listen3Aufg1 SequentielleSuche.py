import random
liste = [0]*20
for i in range(len(liste)):
    liste[i] = random.randint(1,20); print(liste)
print("listen erstellung erfolgreich")


def lineareSuche (zahl):    #funktion wird definiert
    for i in range (len(liste)):
        if liste[i] == zahl:
            return i; print("i")
    return -1
print(lineareSuche(20))     #funktion mit zahl=20 wird als index mit print ausgegeben