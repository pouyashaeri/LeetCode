class Solution:
    # # Time O(n), but Space is still O(n) we need Space O(1)
    # def isPalindrome(self, s: str) -> bool:
    #     cleaned = []
    #     for ch in s:
    #         if ch.isalnum():
    #             cleaned.append(ch.lower())
    #     return cleaned == cleaned[::-1]

    # Space O(1) and Time O(n)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True