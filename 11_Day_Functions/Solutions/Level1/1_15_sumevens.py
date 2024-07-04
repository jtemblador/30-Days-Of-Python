import random

def sum_even(number):
    # to sum even numbers in simply divide by 2
    even_count = number // 2
    # to sum those even numbers we do x(x+1)
    even_sum = (even_count) * (even_count + 1)
    return even_sum


number = random.randint(1,100)
print(f"The sum of all even numbers in {number} is {sum_even(number)}.")
