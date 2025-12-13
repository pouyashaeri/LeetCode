class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()           
        while n!= 1:
            total = 0
            for num in str(n):
                total += int(num)**2
            if total in seen:
                return False
            n = total
            seen.add(n)
        return True