def sum_natural(n: int):
   
    if n == 1:
     return n
    
    if type(n) != int or n < 1:
        return 'Negative or Decimal Numbers are not Natural Numbers'
    # else:
    return n + sum_natural(n-1)

    
n = ''
result = sum_natural(n)
if type(result) == int:
    print(f'The sum of natural numbers up to {n} is {result}')
else:
    print(result)
