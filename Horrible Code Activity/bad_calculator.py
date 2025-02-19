# Bad calculator
print ("Welcome to the Calculator")

# Taking input without separation of concerns
x = input("Enter first number: ")
y = input("Enter second number: ")

# No function reuse, repeated logic
operation = input("Enter operation (x, -, *, /: ")

if operation == "+":
    print("Result: ", float(x) + float(y))
elif operation == "-":
    print("Result: ", float(x) - float(y))
elif operation == "*":
    print("Result: ", float(x) * float(y))
elif operation == "/":
    print("Result: ", float(x) / float(y))
else:
    print("Invalid operation")