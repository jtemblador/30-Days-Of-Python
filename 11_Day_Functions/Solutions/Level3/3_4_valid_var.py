import keyword


def unique_var(name):
    #check if its a string
    if not (isinstance(name, str)):
        return False
    
    #check if its a keyword
    if keyword.iskeyword(name):
        return False
    
    return True 
    

test_cases = [
    "valid_variable",
    "_also_valid",
    "ValidVariable123",
    "1invalid",
    "invalid-variable",
    "lambda",
    "def",
    "var with spaces",
    "",
    "π",  # Unicode character
    "_",
    "__init__",
    "a" * 256,  # Very long name
    123,  # Non-string input
]

for i, test in enumerate(test_cases, 1):
    result = unique_var(test)
    print(f"Test {i}: '{test}'")
    print(f"Is valid Python variable? {result}\n")