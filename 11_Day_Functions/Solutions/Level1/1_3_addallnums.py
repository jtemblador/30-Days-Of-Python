import random

def add_all(numbers):
    sum = 0
    for num in numbers:
        sum += num
    
    return sum

def add_arb(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    
    return sum

# Generate a random number between 1 and 10
size = random.randint(1, 10)

# Create a list of the generated size and fill each element with a random number between 1 and 100
random_list = [random.randint(1, 100) for num in range(size)]

print(f"Random numbers in list")
for i in random_list:
    print(f"{i} + ", end="")
print(f"= {add_all(random_list)}")

#Using arbitrary nubmers now
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)

print("\nArbitrary # of random numbers ")
print(f"{num1} + {num2} + {num3}", end="")
print(f"= {add_arb(num1, num2, num3)}")
