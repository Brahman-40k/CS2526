# Electric Force
from math import pi

q1 = float(input("Enter the charge of 1st particle: "))
q2 = float(input("Enter the charge of 2nd particle: "))
r = float(input("Enter the distance between the two charged particles (in meters): "))
ee = 8.854e-12
force = (q1 * q2) / (4 * pi * ee * (r**2))

print(f"The electric force felt by the particles is {force} N.")