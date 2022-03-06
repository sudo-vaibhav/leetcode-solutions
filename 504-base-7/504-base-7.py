class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        n = abs(num) 
        while(n>0):
            temp = n//7
            r = n%7
            n = temp
            ans=str(r)+ans
        return ("-" if num<0 else "")+ans or "0"