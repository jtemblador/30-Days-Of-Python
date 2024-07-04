import random

def sum_odds(number):
    # sum = 0
    # Checks odd numbers in range of number
    # for i in range(number):
    #     if i % 2 == 1:
    #         sum += i
    # return sum


    # Optimal solution:
    # Sum of odd numbers from 1 to n can be found by (count of odd nums) ^ 2
    # Count of odd nums from 1 to n (inclusive) is: (n + 1) // 2
    odd_count = (number + 1) // 2
    odd_sum   = odd_count ** 2
    return odd_sum

number = random.randint(1,100)

print(f"The sum of all odd numbers in {number} is {sum_odds(number)}.")
