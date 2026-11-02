def binary_search(nums, target) -> tuple[int, int]:
   
    if nums == []:
        return (-1, 0)
        
    if nums[0] == target:
        return (0, 1)
        


    low = 0
    high = len(nums) -1
    comparisons = 0
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            result = mid
            high = mid -1
        if nums[mid] < target:
            low = mid + 1
        if nums[mid] > target:
            high = mid -1
        comparisons += 1
    return (result, comparisons)
        


        


    

nums = [1, 3, 3, 3, 5, 8]
target = 3

result = binary_search(nums, target)
print(result)
        
