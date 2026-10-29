def fibonacci(n: int):
    if n == 0:
        return n
    if n == 1:
        return n
    if n > 20 or n < 0:
        return 'Input  a Number less than or Equal to 20 or Non-Negative'

    if n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = -1
result = fibonacci(n)
if type(result) == int:
    print(f'The Fibonacci number at position {n} is {result}')
else:
    print(result)
    
