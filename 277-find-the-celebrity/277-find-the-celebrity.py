# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        def isCeleb(i):
            for j in range(n):
                if i==j: continue
                else:
                    if knows(i,j) or not knows(j,i):
                        return False
            return True
        
        candidate = 0
        
        for i in range(1,n):
            if knows(candidate,i):
                candidate = i
            else:
                pass
        
        if isCeleb(candidate):
            return candidate
        return -1
                
                        