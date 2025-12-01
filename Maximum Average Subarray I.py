class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        sum_window = sum(nums[:k])
        max_sum = sum_window

        for right in range(k, len(nums)):
            sum_window += nums[right]
            sum_window -= nums[left]
            max_sum = max(sum_window, max_sum)
            left += 1
        
        return max_sum/float(k)