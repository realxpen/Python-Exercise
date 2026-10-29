def is_palindrome(text):
    if len(text) <= 1:
        return text
    
    # if len(text) >= 2:
    return is_palindrome(text[1:]) + text[0]
    
text = 'racecar'
result = is_palindrome(text)
if text == result:
    print(f'{text} is a palindrome.')
else:
    print(f'{text} is Not a palindrome.')

