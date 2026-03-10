# Break and Continue Examples

# Break example
for i in range(10):
    if i == 5:
        break
    print("Break loop:", i)


print("----------------")

# Continue example
for i in range(10):
    if i == 5:
        continue
    print("Continue loop:", i)