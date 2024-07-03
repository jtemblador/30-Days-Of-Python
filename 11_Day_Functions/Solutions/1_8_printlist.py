import random

def print_list(list):
    """Printing elements in a list"""
    for i in list:
        print(f"{i} ", end="")
    print()

stuff = ['a', 'b', 'c', 'd', 'e']
print_list(stuff)