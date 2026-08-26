from random import *
liste = [0]*10;
for i in range(len(liste)):
    liste[i] = randint(1,10)
print(liste)

j=0;b=0;t=0;kleinster=0;schritte=0

for j in range(len(liste)-1):
    kleinster = j
    schritte = schritte +1
    for i in range (j+1,len(liste)):
    
        if liste[kleinster] > liste[i]:
            kleinster = i
    
    (liste[j],liste[kleinster]) = (liste[kleinster], liste[j])     
    print(liste)   
            
print(liste)
print(schritte)
        
    
    