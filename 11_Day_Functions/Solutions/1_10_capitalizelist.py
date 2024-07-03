# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    # Creating a new list to return 
    new_lst = []

    #Appending every element 
    for i in lst:
        new_lst.append(i.title())

    return new_lst

lst = ['soda', 'bottle', 'car', 'chair']
print(f"{capitalize_list_items(lst)}")