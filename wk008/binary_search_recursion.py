def binary_search(nums, target) -> tuple[int, int]:
   
    if nums == []:
        return (-1, 0)
        
    if nums[0] == target:
        return (0, 1)
    
    low = 0
    high = len(nums) -1
    comparisons = 0
    result = -1


    def helper(low, high, comparisons, result):
        if low > high:
            return result, comparisons
        
        mid = (low + high) // 2
        comparisons += 1

        if nums[mid] == target:
            return helper(low, mid - 1, comparisons, mid)
        if nums[mid] < target:
            return helper(mid +1, high, comparisons, mid)
        if nums[mid] > target:
            return helper(low, mid - 1, comparisons, mid)
        
       
    return helper(0, len(nums) - 1, 0, -1)

nums = [1, 3, 3, 3, 5, 8]
target = 3

result = binary_search(nums, target)
print(result)