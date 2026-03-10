# Conditional Statements (if, elif, else)

age = 20

if age < 18:
    print("You are a minor")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")


# Example with user input
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")