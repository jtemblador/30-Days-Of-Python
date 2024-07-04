import random 
from collections import Counter

def print_list(lst):
    for i in lst:
        print(f"{i} ", end="")

def mean(lst):
    """Finding Mean of a list"""
    # get sum
    ttlsum = sum(lst)

    # Sum divided by number of list 
    mean = ttlsum / len(lst)

    return round(mean, 3)

def median(lst):
    """Finding the median of a list"""
    sorted_lst = sorted(lst)
    middle = len(lst) // 2

    if len(lst) % 2 == 0:
        median_value = (lst[middle] + lst[middle - 1]) / 2
    else:
        median_value = lst[middle]

    return median_value

def mode(lst):
    frequency = {}
    for i in lst:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    


    # now get the max value of the list (WE ARE GETTING VALUES NOT THE KEYS)
    max_count = max(frequency.values())

    if max_count == 1:
        return None

    # Now we are creating a list of all numbers with a max_count
    modes = [(key, count) for key, count in frequency.items() if count == max_count]
    
    # return the modes
    return modes




# creating random size
size = random.randint(5, 50)

# creating list with size filled with random numbers
lst = [random.randint(1, 100) for i in range(size + 1)]

print(f"             #'s:  {lst}")
print(f"            Mean: {mean(lst)}")
print(f"          Median: {median(lst)}")
print(f"            Mode: {mode(lst)}")
# print(f"         Range: {rng(lst)}")
# print(f"      Variance: {variance(lst)}")
# print(f"Std. Deviation: {stdDeviation(lst)}")
