# Convert to float immediately during input
firstNum = float(input("Enter the first number: "))
secondNum = float(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = firstNum + secondNum
    print("The Result of the Addition is: ", result)
elif operator == "-":
    result = firstNum - secondNum
    print("The Result of the Subtraction is: ", result)
elif operator == "*":
    result = firstNum * secondNum
    print("The Result of the Multiplication is: ", result)
elif operator == "/":
    # Now this numeric check works perfectly
    if secondNum != 0:
        result = firstNum / secondNum
        print("The Result of the Division is: ", result)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")