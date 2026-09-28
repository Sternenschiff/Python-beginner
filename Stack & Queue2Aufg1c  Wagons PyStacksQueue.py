from adt import *

a = Stack();
a.push(126)
a.push(12)
a.push(153)
a.push(141)
a.push(122)
a.push(1213)
a.push(1343)
a.push(1412)
b = Stack()
c = Stack()
print("stapel a: ",a,"stapel b: " ,b,"stapel c: " ,c) 





print("stapel a: ",a,"stapel b: " ,b,"stapel c: " ,c) 
while not a.isEmpty():
    print("neuer durchlauf")
    c.push(a.pop())
    while not a.isEmpty():
        if a.top() > c.top():
            b.push(c.pop())
            c.push(a.pop())
        else:
            b.push(a.pop())
        print("zeile25", "stapel a: ",a,"stapel b: " ,b,"stapel c: " ,c) 

    print("zeile 27", "stapel a: ",a,"stapel b: " ,b,"stapel c: " ,c) 
    while not b.isEmpty():
        if (b.top() > c.top()):
            a.push(b.pop())
        else:
            a.push(c.pop())
            c.push(b.pop())
        print("zeile34", "stapel a: ",a,"stapel b: " ,b,"stapel c: " ,c)

print("stapel a: ",a,"stapel b: " ,b,"stapel c: " ,c)  
    


