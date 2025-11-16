from typing import List

class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(word)
        return list(res.values())