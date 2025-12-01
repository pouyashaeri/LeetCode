class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        left = 0
        threshold = k * threshold
        sum_window = sum(arr[:k])
        sat_count = 1 if sum_window >= threshold else 0

        for right in range(k, len(arr)):
            sum_window += arr[right]
            sum_window -= arr[left]
            left += 1

            if sum_window >= threshold:
                sat_count += 1
        
        return sat_count