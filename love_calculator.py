print("welcome to LOVE CLACULATOR")
y=input("enter your name ")
h=input("enter his her name")
y=y.lower()
h=h.lower()
t=y.count('t')+h.count("t")
r=y.count('r')+h.count("r")
u=y.count('u')+h.count("u")
e=y.count('e')+h.count("e")
l=y.count('l')+h.count("l")
o=y.count('o')+h.count("o")
v=y.count('v')+h.count("v")
e=y.count('e')+h.count("e")
num=t+r+u+e
tens=num*10
units=l+o+v+e
print(units)
print("your love percentage is",tens+units)
