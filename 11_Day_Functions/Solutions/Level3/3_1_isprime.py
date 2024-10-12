# Write a function called is_prime, which checks if a number is prime.

import random

def is_prime(number):
    # Check if the number is less than 2 (not prime)
    if number < 2:
        return False
    
    # Check for divisibility from 2 to the square root of the number
    # Anything greater than the root would just be more than the number
    # if found to be divisible by any number then the loop return False
    for i in range(2, int(number**0.5) + 1):
        print(f"{number} % {i} = {number % i}")

        if number % i == 0:
            print(f"Divisible by {i}")
            return False
        
    # If no divisors were found, the number is prime
    return True

# Example usage
#num = 17058155121097 #a real big prime number
num = random.randint(2, 9999999999)
print(f"Number is {num}.")

if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")