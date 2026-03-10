# Dictionary Methods

student = {
    "name": "Krish",
    "age": 21,
    "course": "Python"
}

print("Original dictionary:", student)

# Keys
print("Keys:", student.keys())

# Values
print("Values:", student.values())

# Items
print("Items:", student.items())

# Update
student["age"] = 22
print("Updated age:", student)

# Add new key
student["city"] = "Ahmedabad"
print("After adding city:", student)

# Remove key
student.pop("course")
print("After removing course:", student)