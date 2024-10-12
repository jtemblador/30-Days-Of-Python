import random 
import math
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

    return mean

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

def rng(lst):
    """Range is largest value minus the smallest value"""
    return f"{max(lst)} - {min(lst)} = {max(lst) - min(lst)}"

def variance(lst):
    """Calculating variance"""
    # Get mean 
    mn = mean(lst)

    # Creating and calculating a list with the squared difference: (lst[x] - mean)^2 
    var_list = [(x - mn) ** 2 for x in lst]
    
    # Then sum all the values and divide by total numbers 
    return sum(var_list)/len(lst)

def stddev(lst):
    return math.sqrt(variance(lst))


def main():

    # creating random size
    size = random.randint(5, 50)

    # creating list with size filled with random numbers
    lst = [random.randint(1, 200) for i in range(size + 1)]

    print(f"             #'s:  {lst}")
    print(f"           Count: {len(lst)}")
    print(f"            Mean: {mean(lst)}")
    print(f"          Median: {median(lst)}")
    print(f"            Mode: {mode(lst)}")
    print(f"           Range: {rng(lst)}")
    print(f" Popul. Variance: {variance(lst)}")
    print(f"Std. Deviation:   {stddev(lst)}")


if __name__ == '__main__':
    main()