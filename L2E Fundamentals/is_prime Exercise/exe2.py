def is_prime(num: int) -> bool:
    if num == 2: #or num == 3:
        return True
    if num <= 1 or num % 2 == 0:
        return False

    i = 3
  
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def prime_check(num: int):

    if is_prime(num):
        print(f'{num} is Prime')
    else:
        print(f'{num} is Not Prime')

    list_of_non_prime = []
    sum_of_non_primes = 0
    for i in range(2, num+1):
        if not is_prime(i):
            list_of_non_prime.append(i)
            sum_of_non_primes +=i



    print(f"Non-Primes up to {num}: {list_of_non_prime}")
    print(f"Sum of Non-Primes Numbers: {(sum_of_non_primes)}")



prime_check(9)
