class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        return n if n <= 2 else self.climbStairs(n-1)+self.climbStairs(n-2)