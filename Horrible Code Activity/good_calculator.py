# Good calculator

#Returns the sum of two numbers
def add (a,b):
    return a+b

#Returns the difference of two numbers
def subtract(a,b):
    return a-b

#Returns the product of two numbers
def multiply(a,b):
    return a*b

#Returns the quotient of two numbers
def divide(a,b):
    return a/b if b!=0 else "Cannot divide by zero"

#Takes user input and executes the respective calculations
def main():
    print("Welcome to the Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Which operator do you want to use? (+, -, *, /): ")
    operation = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if operator in operation:
        result = operation[operator](num1, num2)
        print("Result: ", result)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
