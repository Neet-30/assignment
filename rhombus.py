from math import sqrt
from math import sin
from math import pow

a=float(input("Enter side:"))
d1=float(input("Enter length of diagonal-1: "))
d2=float(input("Enter length of diagonal-2: "))


a_dia=0.5*d1*d2
print(f"Area of rhombus using diagonal formula: {a_dia}")
a_sin=pow(a,2)*sin(90)
print(f"Area of rhombus using sin formula: {a_sin}")
height=(d1*d2)/(sqrt(pow(d1,2)+pow(d2,2)))
print(f"Height of rhombus: {height}")
side=0.5*(sqrt(pow(d1,2)+pow(d2,2)))
print(f"Side of rhombus is: {side}")
peri=4*a
print(f"Perimeter of rhombus: {peri}")


