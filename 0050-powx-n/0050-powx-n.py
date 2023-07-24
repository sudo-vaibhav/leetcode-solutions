class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def solve(x,n):
            if n==0:
                return 1
            if n%2==1:
                return x*solve(x,n-1)
            temp = solve(x,n//2)
            return temp**2
        
        if n<0:
            return solve(1/x,-n)
        return solve(x,n)