class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countsS = {}
        countsT = {}

        for ch in s:
            countsS[ch] = countsS.get(ch, 0) + 1

        for ch in t:
            countsT[ch] = countsT.get(ch, 0) + 1

        return countsS == countsT