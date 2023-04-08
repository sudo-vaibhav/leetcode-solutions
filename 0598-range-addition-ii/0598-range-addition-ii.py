class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # if not ops: return m*n
        I,J = m,n
        for i,j in ops:
            I = min(I,i)
            J = min(J,j)
            
        return I*J