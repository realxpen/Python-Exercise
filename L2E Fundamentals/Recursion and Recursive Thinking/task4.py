def sum_digits(n):
    # n= abs(n)
    if n < 10:
        return n
    
    last_digit = n % 10
    last_digit_removed = n // 10
    return sum_digits(last_digit_removed) + last_digit

n = -1
# n = abs(n)
result = sum_digits(n)
print(f'The sum of the digits of {n} is {result}')