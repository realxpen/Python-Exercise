word = input("Enter a word: ")

if len(word) <=1:
    print("Invalid Word")
else:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word

    if word == reversed_word:
        result = f"The word '{word}' is a palindrome."
    else:
        result = f"The word '{word}' is not a palindrome."
    print(result)