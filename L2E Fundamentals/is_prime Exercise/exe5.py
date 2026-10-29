
def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i +=2
    return True

def prime_check_interval(n_start: int, n_end: int):

    sum_of_prime_intervals = 0
    i = n_start
    prime_list = []

    while i <= n_end:
        if is_prime(i):
            prime_list.append(i)
            sum_of_prime_intervals += i
        i += 1

    print(f'Prime numbers between {n_start} and {n_end}: {prime_list}')
    print(f'Sum of primes: {sum_of_prime_intervals}')

prime_check_interval(10, 20)

   