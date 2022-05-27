# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        @cache
        def dp(i,j):
            return knows(i,j)
        
        def isCeleb(i):
            for j in range(n):
                if i==j: continue
                else:
                    if dp(i,j) or not dp(j,i):
                        return False
            return True
        candidate = 0
        for i in range(1,n):
            if dp(candidate,i):
                candidate = i
            else:
                pass
        
        if isCeleb(candidate):
            return candidate
        return -1
                
                        