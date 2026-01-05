from typing import List

class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # # Brute-force O(n^2)
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):  # no need to check j < i
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]


        # # Use the "Non-decreasing" property of the problem
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]