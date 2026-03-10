def isAgeValid(age):
    if(age >= 18):
        return true

age = int(input("Enter your age: "))

if isAgeValid:
    print("You're eligible")
else:
    print("You're not eligible")