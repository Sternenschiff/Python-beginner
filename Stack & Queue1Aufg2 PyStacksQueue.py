from adt import *

s = Stack(); a = 0;noten_anzahl = 0;note = 0
while True:
    a = int(input(("gibt deine note ein: ")))
    if (a == -1):
        break
    s.push(a)   
while not s.isEmpty():
    note = note + s.pop(); noten_anzahl += 1
print(note / noten_anzahl)

#int = 8
#str = "8" = "a", "acht"
#float = 8.0000000000
