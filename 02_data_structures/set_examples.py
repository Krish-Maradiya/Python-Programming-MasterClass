# Set Examples

numbers = {1, 2, 3, 4, 4, 5}

print("Original set:", numbers)

# Add element
numbers.add(6)
print("After add:", numbers)

# Remove element
numbers.remove(3)
print("After remove:", numbers)

# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))