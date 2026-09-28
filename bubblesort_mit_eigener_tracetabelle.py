import random
liste = [0]*30
for i in range(len(liste)):
    liste[i] = random.randint(1,100); 
print("listen erstellung erfolgreich")

liste.sort();print(liste)   #liste.sort => sortiert die liste aufsteigend

verlaufa = [0]
verlaufb = [0]
verlaufm = [0]




def binäreSuche(zahl):      #erstellt eine funktion
    a = 0

    b = len(liste)-1
    m = (b+a) // 2  #//keine kommazahlen ; m = mitte der liste
    print("A=",a); verlaufa.append(a)
    print("B=",b); verlaufb.append(b)
    print("M=",m); verlaufm.append(m)
    while liste[m] != zahl and b > a:#solange index m(hälfte) nicht = gesuchte zahl und listenlänge größer a
        
        
        if liste[m] > zahl:                     #wenn eintrag der mitte der liste > zahl, dann      
            b = m-1                   #b wird zur hälfte +1
        else:                                   
            a = m+1                             
        m=(b+a) // 2
        print("A=",a); verlaufa.append(a)
        print("B=",b); verlaufb.append(b)
        print("M=",m); verlaufm.append(m)
    print("A=",a); verlaufa.append(a)
    print("B=",b); verlaufb.append(b)
    print("M=",m); verlaufm.append(m)
    if liste[m] == zahl:
        return m ; 
    else:
        return -1 ; 


print(binäreSuche(2))
print("verlauf a =", verlaufa)
print("verlauf b =", verlaufb)
print("verlauf m =", verlaufm)