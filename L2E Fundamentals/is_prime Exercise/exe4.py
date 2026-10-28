def is_prime(num: int) -> bool:
    
    if num == 2 or num == 3:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    
    i = 3
    while  i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def prime_check(num: int):

    if is_prime(num):
        print(f'{num} is Prime')
    else:
        print(f'{num} is Not Prime')

    divisor_list =[]
    divisor_count = 0
    i = 1
    while i <= num:
        if num % i == 0:
            divisor_list.append(i)
            divisor_count += 1
        i += 1
    print(f'Divisors of {num}: {divisor_list}')
    print(f'Number of divisors: {divisor_count}')

prime_check(14)
