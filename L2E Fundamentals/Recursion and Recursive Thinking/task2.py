def fibonacci(n: int):
    if n < 0:
        return f'{n} is Invalid, Input a Non-Negative Number Instead'
    if n == 0:
        return n
    if n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

n = -1
result = fibonacci(n)

if type(result) == int:
    print(f'The Fibonacci number at position {n} is {result}')
else:
    print(result)
    
