import random

liste = [1,2,3,4,56,6,8,7,4,23,1]
liste = liste*2 #gesammte liste doppeln

for i in range(len(liste)):
    liste[i] = liste[i] * 2 #jedes element * 2
      


import random

zufall = random.randrange(1, len(liste))
liste[zufall] = 1000 #zufallszahl auf 1000 setzen
summe = 0
for i in range(len(liste)):
    summe = summe + liste[i] # jedes einzelne element verdoppeln
print (summe)
print ("summe ist:", summe, "zahlen: ", len(liste))
print (summe / len(liste)) #durchschnitt und summe



klein = 0
groß = 0

for i in range(len(liste)):
    if liste[klein] > liste[i]:#nach kleinstem inhalt suchen
        klein = i
    if liste[groß] < liste[i]: #nach größstem inhalt suchen
        groß = i
print(liste)
print("größter inhalt in i:", groß, "wert:", liste[groß])		#größter inhalt
print("kleinster inhalt in i:", klein, "wert:", liste[klein])	#kleinster inhalt






