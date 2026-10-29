def is_palindrome(text) -> bool:
    if len(text) == 1:
        return True
    
    # print(text[0])
    # print(text[-1])
    if text[0] != text[-1]:
        return False
   
    return is_palindrome(text[1:len(text)-1])


# def palindrome_check(text):
#     if is_palindrome:
#         print(f'{text} is a palindrome.') 
#     else:
#         print(f'{text} is Not a palindrome.')


# palindrome_check('racecar')


print(is_palindrome("ar"))
