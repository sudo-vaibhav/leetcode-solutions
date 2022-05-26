# Binary search approach
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,num
        while l<=r:
            guess = (l+r)//2
            t = guess**2
            if t>num:
                r = guess-1
            elif t<num:
                l = guess+1
            else:
                return True
        
        return False