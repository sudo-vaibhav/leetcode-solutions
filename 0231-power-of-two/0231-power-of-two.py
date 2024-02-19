class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        n&=n-1
        if n==0:
            return True
        return False