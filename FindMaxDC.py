def find_max(nums):
    if len(nums) == 1:
        return nums[0]
    
    mid = len(nums) // 2
    max_left = find_max(nums[:mid])
    max_right = find_max(nums[mid:])
    return max(max_left, max_right)

print(find_max([1,6,152,4,8,99,7,9]))