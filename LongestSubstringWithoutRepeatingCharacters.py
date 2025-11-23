from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = ""
        for i in range(len(s)):
            substr = ""
            left = i
            while s[left] not in substr:
                substr += substr.join(s[left])
                if left < len(s) - 1:
                    left +=1
                if left > len(s):
                    break
            if len(max_substr) < len(substr):
                max_substr = substr
        return len(max_substr)