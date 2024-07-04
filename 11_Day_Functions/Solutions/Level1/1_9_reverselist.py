def reverse_list(lst):
    new_list = []
    # start value (starting at last index), stop value (stop value, up to 0 won't include -1, step backward  
    for i in range(len(lst) -1, -1, -1):
        new_list.append(lst[i])

    return new_list

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]