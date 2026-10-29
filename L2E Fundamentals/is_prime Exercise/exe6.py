def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def prime_check(n_len: int):
    
    prime_list = []
    sum_of_primes = 0

    count = 1
    i = 2

    while count <= n_len:
        if is_prime(i):
            prime_list.append(i)
            sum_of_primes += i
            count += 1
    
        if i == 2:
            i = 3
        else:
            i+= 2
    
    print(f'First {n_len} prime numbers is: {prime_list}')
    print(f'Sum of primes: {sum_of_primes}')

prime_check(5)