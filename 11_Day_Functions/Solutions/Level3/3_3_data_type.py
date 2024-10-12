# Write a function which checks if all the items of the list are of the same data type.

import random

def same_type(lst):

    if len(lst) == 0:
        return "Empty List"
    
    # get the fist type of the list
    first_type = type(lst[0])

    for i in lst[1:]:
        # compare it with every other element in list 
        if type(i) != first_type:
            return False
    
    return True

test_cases = [
    [1, 2, 3, 4, 5],        #True
    [1.0, 2.0, 3.0, 4.0],   #True
    ["a", "b", "c", "d"],   #True
    [True, False, True],    #True
    [1, "2", 3, "4"],       #False
    [],                     #Empty
    [1],                    #True
    [1, 2, 3, 4.0],         #False
    [[1,2], [3,4], [5,6]],  #True
    [{"a": 1}, {"b": 2}],   #True
    [1, 1, 1, 2]            #True
]

for i, test in enumerate(test_cases, 1):
    result = same_type(test)
    print(f"Test {i}: {test}")
    print(f"All same type? {result}\n")