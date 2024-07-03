import random

def remove_all_instances(lst, itm):
    while itm in lst:
        lst.remove(itm)
    return lst

size = random.randint(1, 15)
num_remove = random.randint(1, 15)

# Filling random sized list with randomly sized integers
lst = [random.randint(1, 10) for num in range(size)]

print(f"Original list\n{lst}")
print(f"Removing #{num_remove}...")
print(remove_all_instances(lst, num_remove))
