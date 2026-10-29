def countdown(n):
    print(n)

    # recursive function call
    return countdown(n-1)
countdown(10)



# countdown(10)

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# num = 3
# print("The factorial of", num, "is", factorial(num))