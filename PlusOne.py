from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for d in range(len(digits)-1, -1, -1):
            if digits[d] < 9:
                digits[d] += 1
                return digits
            digits[d] = 0
        return [1] + digits