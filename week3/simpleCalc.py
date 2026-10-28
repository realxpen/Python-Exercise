total = 0.0
history = []

while True:
    entry = input("Enter an operation (+ 5, -, *, /), 'undo', or 'quit': ").strip()
    if entry.lower() == 'quit':
        break
    if entry.lower() == 'undo':
        if history:
            total = history.pop()
        else:
            print("Nothing to undo.")
        print("Result:", total)
        continue

    parts = entry.split()
    if len(parts) != 2 or parts[0] not in ['+', '-', '*', '/']:
        print("Invalid input. Enter an operator and number, such as '+ 5'.")
        continue

    try:
        number = float(parts[1])
    except ValueError:
        print("Invalid number. Please enter a numeric value.")
        continue

    operator = parts[0]
    if operator == '/' and number == 0:
        print("Error: Cannot divide by zero.")
        continue

    history.append(total)
    if operator == '+':
        total += number
    elif operator == '-':
        total -= number
    elif operator == '*':
        total *= number
    else:
        total /= number
    print("Result:", total)