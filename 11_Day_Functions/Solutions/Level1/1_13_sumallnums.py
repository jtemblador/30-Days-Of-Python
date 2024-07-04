import random

def sum_of_numbers(num):
    #sum of an arithmetic sequence:
    return (num * (num + 1)) // 2

a = random.randint(1,1000)
b = random.randint(1,1000)
c = random.randint(1,1000)

print("Sum of all numbers")
print(f"{a} is {sum_of_numbers(a)}")
print(f"{b} is {sum_of_numbers(b)}")
print(f"{c} is {sum_of_numbers(c)}")

