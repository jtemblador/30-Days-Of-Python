import random
import math

def quadratic(a, b, c):
    """"""
    # Calulate discriminant 
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real roots
        root1 = ((-b + math.sqrt(discriminant)) / (2*a))
        root2 = ((-b - math.sqrt(discriminant)) / (2*a))
        return (root1, root2)

    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return (root, )
    else:

        # Complex roots
        real = -b / 2*a
        imag = math.sqrt(abs(discriminant)) / (2*a)
        return (complex(real, imag), complex(real, -imag))
    
a = random.randint(-10, 10)
b = random.randint(-10, 10)
c = random.randint(-10, 10)

print(f"Solving quadratic equation for: {a}x^2 + {b}x + {c} = 0")
print(f"Roots are: {quadratic(a, b, c)}")
