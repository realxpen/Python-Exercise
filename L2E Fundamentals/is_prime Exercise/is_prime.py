def is_prime(num: int) -> bool:
    
    if num == 2:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    i = 3
    while i*i <= num:
        if num % i == 0:
            return False
        i += 2 #we added two because even numbber cannot divide odd number so we just skip the even number trying to divide odd number 
    return True


def prime_checker(limit: int):
    prime_numbers_list = []
    prime_total = 0

    for i in range(2, limit):
        if  is_prime(i):
            prime_numbers_list.append(i)
            prime_total +=1
    return prime_total, prime_numbers_list



target_num = int(input("Input Number to Check: "))
total_prime, prime_list = prime_checker(target_num)


print(f"Primes up to: {target_num} {prime_list}")
print(f"Sum of primes: {total_prime}")