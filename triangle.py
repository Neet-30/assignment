from math import sqrt
from math import sin
a=float(input("Enter side1: "))
b=float(input("Enter side2: "))
c=float(input("Enter side3: "))
h=float(input("Enter height: "))

area=0.5*b*h
print(f"Area of traingle: {area}")
peri=a+b+c
print(f"Perimeter of triangle: {peri}")
semi=peri*0.5
print(f"Semi-perimeter of triangle: {semi}")
a_sin=0.5*a*b*sin(30)
print(f"Area of triangle with sin formula: {a_sin}")
heron=sqrt(semi*(semi-a)*(semi-b)*(semi-c))
print(f"Area of triangle with heron's formula: {heron}")
