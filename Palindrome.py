class Solution:

    def reformatString(self, s):
        ns = ''
        s = s.lower()
        for i in s:
            if i >= 'a' and i <= 'z':
                ns = ns + i
            if i >= '0' and i <= '9':
                ns = ns + i
        return ns

    def isPalindrome(self, s: str) -> bool:
        ns = self.reformatString(s)
        rs = ''

        for i in range(len(ns)-1, -1, -1):
            # print(i)
            rs = rs + ns[i]

        if rs == ns:
            return True

        return False
        
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("BYE EYB?"))
