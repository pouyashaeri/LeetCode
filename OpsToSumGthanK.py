class Solution:
    def greaterThanK(self, k: int) -> int:
        if k <= 1:
            return 0
        
        best = float("inf")
        for x in range(1, k+1):
            inc = x - 1
            if x >= k:
                dup =0
            else:
                dup = (k - x + x - 1) // x
            ops = inc + dup
            if ops < best:
                best = ops

            if inc > best:
                break
        return best
    
sol = Solution()
print(sol.greaterThanK(11))