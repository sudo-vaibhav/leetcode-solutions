class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = n-1
        
        v = time//p
        left = time-v*p
        if v%2==0:
            # will be from left end
            return 1+left
        else:
            return n-left
            