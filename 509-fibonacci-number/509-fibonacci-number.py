class Solution:
    @lru_cache(maxsize=3)
    def fib(self, n: int) -> int:
        return n if n<=1 else self.fib(n-1)+self.fib(n-2) 