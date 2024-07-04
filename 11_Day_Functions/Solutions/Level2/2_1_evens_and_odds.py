import random

def evens_and_odds(number):
    """This will count all even and odd numbers up to a certain number"""
    even_count = number // 2
    odd_count  = (number + 1) // 2
    return even_count, odd_count

number = random.randint(1,100)
evens, odds = evens_and_odds(number)
print(f"    Number:  {number}")
print(f"Odds count:  {evens}")
print(f"Evens cout:  {odds}")
