#!/usr/bin/python3

# This is a new approach to answer the question on area of a circle

# Owner: Moshood


def area_of_a_circle ():
    if Radius < 0:
        return "Radius cannot be negative."
    else:
        import math
        Area = math.pi * (Radius ** 2)
        return Area


Radius = float(input("Enter the radius of the circle: "))


Area = area_of_a_circle ()
print(f"The area of the circle with radius {Radius} is {Area:.2f}")