class Solution:
    def tribonacci(self, n: int) -> int:
        n1,n2,n3 = 0,1,1
        
        if n==0:
            return 0
        if n<=2:
            return 1
        c = 2
        while True:
            c+=1
            newNum = n1+n2+n3
            if c==n:
                return newNum
            n1 = n2
            n2 = n3
            n3 = newNum
        