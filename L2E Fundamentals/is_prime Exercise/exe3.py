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
        original_num = num
        

        if is_prime(num):
            print(f'{num} is Prime')
        else:
            print(f'{num} is Not Prime')

        while (is_prime(num) == False) and (num >= 2):
            num -=1
        if num <= 1:
            print('No prime number found.')
        else:
            if is_prime(num):
                print(f'Largest prime up to {original_num}: {num}')
            
prime_check(13)
