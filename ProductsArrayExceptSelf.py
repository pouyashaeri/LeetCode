from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)           # n = 4 , nums = [1,2,4,6]
        
        right = n * [1]         # right = [48,24,6,1]
        for i in range(n-2,-1,-1):  # O(n)
            right[i] = right[i+1] * nums[i+1]

        left = n * [1]          # left = [1,1,2,8]
        for i in range(1, n):       # O(n)
            left[i] = left[i-1] * nums[i-1]
        
        result = []
        for i in range(n):
            result.append(left[i] * right[i])
        
        return result