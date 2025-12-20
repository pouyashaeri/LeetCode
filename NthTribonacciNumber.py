class Solution:
    # # Recursive solution has O(3**n) Time limit in Leetcode #1137
    # def tribonacci(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 1
    #     return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        t_0, t_1, t_2 = 0, 1, 1
        for _ in range(n-2):
            t_2, t_1, t_0 = t_2 + t_1 + t_0, t_2, t_1
        return t_2