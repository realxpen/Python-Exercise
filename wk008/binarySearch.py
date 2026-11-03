def binary_search(nums, target) -> tuple[int, int]:
    low = 0
    high = len(nums) - 1
    comparisons = 0
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        if nums[mid] == target:
            result = mid
            high = mid - 1  # Continue searching left to find the FIRST occurrence
        elif nums[mid] < target:
            low = mid + 1 # Continue searching right 
        else:
            high = mid - 1
            
    return (result, comparisons)

nums = [1, 3, 3, 3, 5, 8]
target = 3

result = binary_search(nums, target)
print(result)