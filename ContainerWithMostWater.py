from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_amount = 0
        while left < right:
            max_amount = max(max_amount, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1
        return max_amount
