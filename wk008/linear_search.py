def linear_search(numbers: list[int], target: int) -> int:
    
    # Check for Empty List and what to Return
    if not numbers:
        return "This is an Empty List"
    
    # for num in range(len(numbers)):
    #     if numbers[num] == target:
    #         return f'Target {target} Found at Index {num}'
    # return f"-1\nTarge {target} Not in the List"

    for index, num in enumerate(numbers):
        if num == target:
            return f'Target {target} Found at Index {index}'
    return f"-1\nTarget {target} Not in the List"



numbers = []
target = 2
result = linear_search(numbers, target)
print(result)