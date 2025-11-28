from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # include the i in subset
            subset.append(nums[i])
            backtrack(i + 1)

            # exclude the i from subset
            subset.pop()
            backtrack(i + 1)
            
        backtrack(0)
        return res