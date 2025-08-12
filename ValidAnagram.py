class Solution:

    def sortString(self, s):
        return ''.join(sorted(s))

    def isAnagram(self, s: str, t: str) -> bool:
        s = self.sortString(s)
        t = self.sortString(t)
        if s == t:
            return True
        return False