from typing import List

# Neet code: edge case handeled by len < 3
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) <= 3:
#             return max(nums)
#         def rob1(nums):
#             prev1, prev2 = 0, 0
#             for num in nums:
#                 prev1, prev2 = max(num + prev2, prev1), prev1
#             return prev1
#         return max(rob1(nums[1:]), rob1(nums[:len(nums)-1]))

# Leet code style main:
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robone(nums[1:]), self.robone(nums[:-1]))

    def robone(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1) , prev1
        return prev1