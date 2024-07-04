def is_empty(n):

    if n:
        return False
    else:
        return True
    
print(is_empty([]))  # True, since the list is empty
print(is_empty([1, 2, 3]))  # False, since the list is not empty
print(is_empty(""))  # True, since the string is empty
print(is_empty("hello"))  # False, since the string is not empty
print(is_empty({}))  # True, since the dictionary is empty
print(is_empty({"key": "value"}))  # False, since the dictionary is not empty
print(is_empty(set()))  # True, since the set is empty
print(is_empty({1, 2, 3}))  # False, since the set is not empty