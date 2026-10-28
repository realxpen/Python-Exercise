limit = int(input("Input a Number to Check it its a Prime:  "))

sum_of_primes = 0
prime_list = []


for num in range(2, limit + 1):
    is_prime = True

    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
            
    if is_prime:
        sum_of_primes += num
        prime_list.append(num)


if limit in prime_list:
    print(f"{limit} is prime.")
else:
    print(f"{limit} is not prime.")

print(f"Primes up to {limit}: {prime_list}")

print(f"Sum of primes: {sum_of_primes}")