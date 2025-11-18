from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        result = []
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + 1 in nums:
                    length += 1
                    num += 1
                result.append(length)
        return max(result)