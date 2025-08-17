from math import sqrt
from math import pow
a=float(input("Enter side of square: "))
area=pow(a,2)
peri=4*a
dia=sqrt(2*a)
print(f"Area of square: {area}")
print(f"Perimeter of square: {peri}")
print(f"Diagonal of square: {dia}")