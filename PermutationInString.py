class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = [0] * 26
        count_window = [0] * 26

        for ch in s1:
            count_s1[ord(ch) - ord('a')] += 1
        
        left = 0
        right = len(s1)

        for i in range(len(s2)):
            count_window[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                count_window[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if count_window == count_s1:
                return True

        return False