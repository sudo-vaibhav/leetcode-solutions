class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        d1 = abs(fx-sx)
        d2 = abs(fy-sy)
        
        d = max(d1,d2)
        if d==0: return t!=1
        if d>t: return False
        return True