input_string = input("Enter a string of parentheses: ")

balance = 0
is_balanced = True

for char in input_string:
    if char == '(':
        balance += 1
    elif char == ')':
        balance -= 1
    
    if balance < 0: #balance > 0 char not in '()':
        is_balanced = False
        break

if (is_balanced and balance == 0):
    print("Balanced parentheses.")
else:
    print("Unbalanced parentheses.")
