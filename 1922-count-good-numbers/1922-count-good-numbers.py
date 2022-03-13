class Solution:
    def countGoodNumbers(self, n: int) -> int:
        _4 = n//2
        _5 = n-_4
        MOD = int((pow(10,9)+7))
        def f(x,n):
            if n==0:return 1
            if(n%2==1):
                return ((f(x,n-1)%MOD)*x%MOD)%MOD
            else:
                return ((f(x,n//2)%MOD)**2)%MOD
        return (f(4,_4)*f(5,_5))%MOD
        