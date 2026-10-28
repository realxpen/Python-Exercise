def find_missing(nums):
    # result = []
    for i in range(len(nums)-1):

        if nums[i+1] - nums[i] != 1:
            # return nums.insert(nums[i+1], num[i] + 1)
            return nums[i] + 1