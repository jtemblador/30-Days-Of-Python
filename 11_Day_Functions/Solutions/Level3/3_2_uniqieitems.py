# Write a functions which checks if all items are unique in the list.

import random 

def unique(lst):
    
    # Use a dictionary as a hash table for O(n) time and space complexity 
    seen = {}

    # iterate through every element in the list
    for i in lst:
        # uses hash based lookup system
        if i in seen:
            # false if found 
            return False
        else:
            # add to dictionary
            seen[i] = True
    
    return True 

# This puts lst in a set which removes all duplicate values, 
# if both lists have the same length then all items unique (True)
def unique_set(lst):
    return len(lst) == len(set(lst))

lst = [random.randint(5,100) for i in range(10)]

print(f"List: {lst}")
print(f"All unique? {unique(lst)}")
