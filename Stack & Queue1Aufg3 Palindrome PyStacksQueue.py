from adt import *

palin = input("Gib dein Palindrom ein: ")

s = Stack()
is_palin = ""

for i in palin.lower():
    if i != " ":
        s.push(i)

while not s.isEmpty():
    is_palin += s.pop()

if is_palin == palin.lower().replace(" ", ""):
    print("Palindrom!")
else:
    print("Nope")


    
    