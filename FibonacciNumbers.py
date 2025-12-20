class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        f_0, f_1 = 0, 1
        for _ in range(n-1):
            f_0, f_1 = f_1, f_0 + f_1
        return f_1
    
    # # Recursive Method O(2**n)
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return self.fib(n-1) + self.fib(n-2)