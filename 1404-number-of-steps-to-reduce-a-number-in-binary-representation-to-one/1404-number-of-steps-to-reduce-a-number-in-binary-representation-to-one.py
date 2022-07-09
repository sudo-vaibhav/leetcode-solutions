class Solution:
    def numSteps(self, s: str) -> int:
        
        x = int(s,2)
        
        
        steps = 0
        while x!=1:
            if x%2==1:
                x+=1
            else:
                x//=2
            steps+=1
        return steps
        