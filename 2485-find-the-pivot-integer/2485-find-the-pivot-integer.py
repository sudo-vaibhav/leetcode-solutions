class Solution:
    def pivotInteger(self, n: int) -> int:
#         x*(x+1)/2=n*(n+1)//2 - (x-1)*x//2
        
#         x*(2x)/2 = n*(n+1)
        
        temp = ((n*(n+1))//2)**0.5
        if temp==int(temp):
            return int(temp)
        return -1
        