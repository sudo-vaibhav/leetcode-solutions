class Solution:
    def canMeasureWater(self, j1: int, j2: int, tc: int) -> bool:
        if j1+j2<tc: return False
        f = gcd(j1,j2)
        return (tc//f)==(tc/f)
        