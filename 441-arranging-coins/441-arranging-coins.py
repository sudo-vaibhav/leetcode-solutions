class Solution:
    def arrangeCoins(self, f: int) -> int:
#         n*n + n - 2f = 0
#         
        return floor((-1+sqrt(1+8*f))//2)