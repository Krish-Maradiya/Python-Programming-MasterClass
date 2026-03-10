# Dictionary, Tuple, and Set

# Dictionary
student = {
    "name": "Krish",
    "age": 21,
    "course": "Python"
}

print("Student Name:", student["name"])
print("Student Age:", student["age"])

# Tuple
coordinates = (10, 20, 30)

print("Tuple values:")
for value in coordinates:
    print(value)

# Set
numbers = {1, 2, 3, 4, 4, 5}

print("Set values:", numbers)

numbers.add(6)
print("After adding:", numbers)