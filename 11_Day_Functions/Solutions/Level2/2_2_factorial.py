import random

def factorial(num):
    fact = 1
    # We add one to the number because range does 'i > num' but we need 'i >= num'
    for i in range(2, num + 1):
        fact *= i
    
    return fact

number = random.randint(1, 20)
print(f"{number}! = {factorial(number)}")