Input_list = [12, 5, 27, 8, 14]

if not Input_list:
    print("The list is empty.")

else:
 #check for largest and smallest numbers
    largest = Input_list[0]
    smallest = Input_list[0]
    for i in Input_list:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i
    print(f'Largest number: {largest}')
    print(f'Smallest number: {smallest}')

    #check for total and average
    total = 0
    for i in Input_list:
        total += i
    print(f'Total: {total}')

    average = total / len(Input_list)
    print(f'Average: {average:.1f}')
