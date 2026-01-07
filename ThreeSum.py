import numpy as np
from typing import List

class Solution:
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            res = []

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                if nums[i] > 0:
                    break

                target = -nums[i]
                j, k = i + 1, len(nums) - 1

                while j < k:
                    if nums[j] + nums[k] == target:
                        res.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                    
                    elif nums[j] + nums[k] < target:
                        j += 1
                    else:
                        k -= 1
            
            return res


# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
