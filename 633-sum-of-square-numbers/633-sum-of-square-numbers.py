class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        A = floor(c**(0.5))
        
        for a in range(0,A+1):
            asq = a**2
            rest = c- asq
            temp = rest**(0.5) 
            if int(temp)==temp:
                return True
        return False