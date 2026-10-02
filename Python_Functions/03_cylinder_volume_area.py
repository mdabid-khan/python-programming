import math


def volume(radius, height):
    return math.pi * radius * radius * height


def surfaceArea(radius, height):
    return 2 * math.pi * radius * (radius + height)


radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

print("Volume:", volume(radius, height))
print("Surface Area:", surfaceArea(radius, height))