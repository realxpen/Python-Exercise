def power(base, exponent):
    if exponent == 0:
        return 1
    if base == 0:
        return base
    if exponent < 0:
        exponent = abs(exponent)

    return base * power(base, exponent -1)

base = int(input('Enter Your Base Number: '))
exponent = int(input('Input Your Exponent: '))

result = power(base, exponent)
print(f'{base} raised to the power of {exponent} is {result}')