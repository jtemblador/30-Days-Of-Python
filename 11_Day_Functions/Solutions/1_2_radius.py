import math 
import random 

def area_of_circle(radius):
    return math.pi * radius * radius

radius = round(random.uniform(1,10), 2)
print(f"Circle with Radius {radius}cm is {round(area_of_circle(radius), 3)}cm in area.")
