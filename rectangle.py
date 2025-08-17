from math import pow
from math import sqrt

l=float(input("Enter length of rectangle: "))
b=float(input("Enter breadth: "))
h=float(input("Enter height: "))

area= l*b
print(f"Area of rectangle is: {area}")
peri=2*(l+b)
print(f"Perimeter of rectangle: {peri}")
dia=sqrt(pow(l,2)+pow(b,2))
print(f"Diagonal of rectangle: {dia}")
a_walls=2*h*(l+b)
print(f"Area of 4walls: {a_walls}")