class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        vowels = {'a','e','i','o','u'}
        
        window = s[:k]

        count_window = 0

        for ch in window:
            if ch in vowels:
                count_window += 1

        count_max_window = count_window
        
        for right in range(k, len(s)):
            if s[right] in vowels:
                count_window += 1 
            if s[left] in vowels:
                count_window -= 1
            count_max_window = max(count_max_window, count_window)
            left += 1

        return count_max_window