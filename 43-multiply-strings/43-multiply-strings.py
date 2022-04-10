class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for idx,b in enumerate(num2[::-1]):
            base = 10**idx
            tempans = int(num1)*int(b)
            ans+=base*tempans
            
        return str(ans)