import random

def add_numbers(n1, n2):
    return n1 + n2

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

print(f"Adding Numbers {num1} + {num2} = {add_numbers(num1, num2)}")