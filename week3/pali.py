def is_palindrome(sentence):
	left = 0
	right = len(sentence) - 1

	while left < right:
		while left < right and not sentence[left].isalnum():
			left += 1
		while left < right and not sentence[right].isalnum():
			right -= 1

		if sentence[left].lower() != sentence[right].lower():
			return False

		left += 1
		right -= 1
		
	return True


sentence = input()
if is_palindrome(sentence):
	print("Palindrome")
else:
	print("Not a palindrome")
