class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        m,n = len(mat),len(mat[0])        
        def check(startI,startJ):
            disp = 0
            while startI+disp<m and startJ+disp<n:
                if mat[startI][startJ]!=mat[startI+disp][startJ+disp]:
                    raise "unequal"
                disp+=1
        try:
            for start in range(m):
                check(start,0)
            for start in range(n):
                check(0,start)
        except:
            return False
        return True
        