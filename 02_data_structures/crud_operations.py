# CRUD Operations Example (Create, Read, Update, Delete)

students = ["Krish", "Rahul", "Amit"]

# CREATE
students.append("Priya")
print("After Create:", students)

# READ
print("First student:", students[0])

# UPDATE
students[1] = "Rohan"
print("After Update:", students)

# DELETE
students.remove("Amit")
print("After Delete:", students)