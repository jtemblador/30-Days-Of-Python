import random

def c_to_f(cel):
    return (cel * 9/5) + 32

celius = round(random.uniform(0, 45), 2)

print(f"{celius} Celsius = {round(c_to_f(celius), 2)} Fahrenheit")