operator = input("Enter an operator (+, -, *, /, %): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# if num1 and num2 != float or int:
#     print("Input only numbers")
if operator == "+":
    aResult = num1 + num2
    print('Addition Result: ', aResult )
elif operator == '-':
    sResult = num1-num2
    print('Subtraction Result: ', sResult)
elif operator == '*':
    mResult = num1 * num2
    print('Multiplication Result:' , mResult)
elif operator == '%':
    mdResult = num1 % num2
    print('Modulo Result: ', mdResult)
elif operator == '/' and num2 !=0:
    dResult = num1 / num2
    print('Division result: ',dResult)
elif num2 == 0 and operator == '/':
    print('Cannot Divide by zero(0)')
else:
    print('Invalid Operator')
