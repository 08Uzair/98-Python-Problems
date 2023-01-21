import math
a=int(input("Entre the value of a : "))
b=int(input("Entre the value of b : "))
c=int(input("Entre the value of c : "))
d=(b**2)-4*a*c
e=d**0.5
f1=(-b+e)
f2=(-b-e)
g1=(f1/(2*a))
g2=(f2/(2*a))
print(f"The Roots of the given Quadratic Equation are {g1} and {g2}")