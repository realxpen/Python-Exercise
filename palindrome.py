word = input("Enter a word to check if it is a palindrome: ")
if len(word) < 2:
    print("The word is too short to check for palindrome.")
else:
    reversed_word = word[-1::-1]
    if word == reversed_word:
        print(f'{word} is a palindrome.')
    else:
        print(f'{word} is not a palindrome.')
