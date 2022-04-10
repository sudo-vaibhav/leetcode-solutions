class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for idx,b in enumerate(num2[::-1]):
            base = 10**idx
            tempans = 0
            c=0
            mul = 1
            for a in num1[::-1]:
                f = int(a)*int(b)
                f+=c
                c = f//10
                tempans +=mul*(f%10)
                mul*=10
            tempans+=c*mul    
            ans+=base*tempans
            
        return str(ans)