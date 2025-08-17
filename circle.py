from math import pi
from math import pow
r=float(input("Enter radius of circle: "))

area=pi*pow(r,2)
print(f"Area of circle: {area}")
semi=0.5*area
print(f"Area of semi-circle:{semi}")
qua=0.25*area
print(f"Area of quadrant: {qua}")
peri=2*pi*r
print(f"Perimeter of circle: {peri}")
p_semi=(pi*r)+(2*r)
print(f"Perimeter of semi-circle: {p_semi}")