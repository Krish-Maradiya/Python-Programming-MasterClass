"""
Different types of function arguments
"""

# Positional arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Krish", 22)


# Default arguments
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Rahul")


# Keyword arguments
def student_info(name, course):
    print(f"{name} is studying {course}")

student_info(course="Python", name="Krish")
