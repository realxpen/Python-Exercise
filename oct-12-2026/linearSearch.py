input_list = [14, 7, 22, 9, 7, 31]

if not input_list:
    print("The list is empty.")
else:
    # Look for target index
    target = int(input("Enter a number to search for: "))
    found = False
    for index in range(len(input_list)):
        
        if input_list[index] == target:
            print(f"Target: {target}\nFound at index {index}.")
            found = True
            break
    if not found:
        print(f"Target: {target}\nTarget Not found.")