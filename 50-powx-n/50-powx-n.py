class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n *= -1
        def powerRecursive(x,n):
            if n==0:
                return 1
            if n%2==1:
                return x*powerRecursive(x,n-1)
            else:
                return powerRecursive(x,n//2)**2
        
        return powerRecursive(x,n)
        