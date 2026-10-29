def sum_natural(n: int):
   
    if n == 1:
     return n
    
    if n < 1 or type(n) != int:
        return 'Negative or Decimal Numbers are not Natural Numbers'
    # else:
    return n + sum_natural(n-1)

    
n = 2
result = sum_natural(n)
if type(result) == int:
    print(f'The sum of natural numbers up to {n} is {result}')
else:
    print(result)
