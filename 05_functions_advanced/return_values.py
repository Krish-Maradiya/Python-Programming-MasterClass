"""
Functions that return values
"""

def add(a, b):
    return a + b

result = add(10, 5)
print("Addition:", result)


def is_even(number):
    return number % 2 == 0

num = 8

if is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")