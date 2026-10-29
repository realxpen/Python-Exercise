def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if num <= 1 or num % 2 == 0:
        return False

    i = 3
  
    while i*i <= num:
        if num % i == 0:
            return True
        i += 2
    return True


def prime_check(num: int):

    if is_prime(num):
        print(f'{num} is Prime')
    else:
        print(f'{num} is Not Prime')

    list_of_prime = []
    prime_count = 0
    for i in range(2, num=1):
        if is_prime(i):
            list_of_prime.append(i)
            prime_count += 1


    print(f"Primes up to {num}: {list_of_prime}")
    print(f"Number of Primes: {prime_count}")



is_prime(13)
