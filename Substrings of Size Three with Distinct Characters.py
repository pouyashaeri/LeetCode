class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        for i in range(len(s) - 2):
            window = s[i:i + 3]
            if len(set(window)) == 3:
                count += 1
            
        return count