import random

def calculate_slope(x1, x2, y1, y2):
    if x1 == x2:
        raise ValueError("The slope is a vertical line. No Slope.")
    else:
        return (y2 - y1)/ (x2 - x1)

x1 = random.randint(1,10)
x2 = random.randint(1,10)
y1 = random.randint(1,10)
y2 = random.randint(1,10)

try:
    print(f"Points: ({x1}, {y1}) ({x2}, {y2}).")
    print(f"Slope:  {round(calculate_slope(x1, x2, y1, y2), 2)}")
except ValueError as e:
    print(e)
