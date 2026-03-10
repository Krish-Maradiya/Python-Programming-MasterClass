"""
Recursion Examples
A recursive function calls itself
"""

# Factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# Fibonacci using recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 6:", fibonacci(6))