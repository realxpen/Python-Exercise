def intersection(a, b):
    result = []

    for item in a:

        if item in b and item not in result:
            result.append(item)
    return result 



print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
print(intersection([1, 2, 2, 3], [2, 2, 3]))     # Output: [2, 3]
print(intersection([3, 1, 2], [1, 3]))           # Output: [3, 1] (Keeps 'a' order!)
print(intersection([1, 2], [3, 4]))  


    # print(f'{myset_a} and {myset_b}')
# intersection([1, 2, 2, 3, 4], [3, 4, 5, 6])