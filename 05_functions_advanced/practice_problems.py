"""
Practice Problems
"""

# 1. Function to find the largest of three numbers
def largest(a, b, c):
    return max(a, b, c)

print("Largest:", largest(10, 25, 7))


# 2. Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

print("Vowels:", count_vowels("Python Programming"))


# 3. Recursive function to calculate sum of numbers

def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

print("Sum of first 5 numbers:", sum_numbers(5))