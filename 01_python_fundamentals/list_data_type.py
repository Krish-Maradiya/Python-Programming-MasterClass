# List Data Type

fruits = ["apple", "banana", "mango", "orange"]

print("Fruit list:", fruits)

# Access item
print("First fruit:", fruits[0])

# Add item
fruits.append("grapes")
print("Updated list:", fruits)

# Remove item
fruits.remove("banana")
print("After removing banana:", fruits)

# Loop through list
for fruit in fruits:
    print(fruit)