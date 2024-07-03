import random

def sum_of_numbers(num):
    return (num * (num + 1)) // 2

a = random.randint(1,1000)
b = random.randint(1,1000)
c = random.randint(1,1000)

print("Sum of all numbers")
print(f"{a} is {sum_of_numbers(a)}")
print(f"{b} is {sum_of_numbers(b)}")
print(f"{c} is {sum_of_numbers(c)}")

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon