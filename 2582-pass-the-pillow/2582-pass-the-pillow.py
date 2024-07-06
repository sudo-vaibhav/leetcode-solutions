class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        v = time//(n-1)
        left = time-v*(n-1)
        return 1+left if v%2==0 else n-left
            