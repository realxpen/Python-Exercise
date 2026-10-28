matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]

row_number = 1

for row in matrix:
    total_sum = 0
    # for r in range(len(row)-len(row)):
    for num in row:

        total_sum += num
    
    # for i in range(len(row)+1):
    #     i +=i

    
    print(f'Row {row_number} total: {total_sum}')
    row_number += 1
    


