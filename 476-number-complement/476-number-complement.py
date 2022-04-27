class Solution:
    def findComplement(self, num: int) -> int:
        t = log(num,2)
        if t==int(t):
            t+=1
        else:
            t = ceil(t)
        
        f = int((2**t)-1)
        
        return f^num