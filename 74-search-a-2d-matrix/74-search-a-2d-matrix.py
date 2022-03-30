class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t=0
        b=len(matrix)-1
        l=0
        r=len(matrix[0])-1
        
        while t<=b:
            m = t+(b-t)//2
            if target>=matrix[m][0] and target<=matrix[m][-1]:
                break
            else:
                if target<matrix[m][0]:
                    b=m-1
                else:
                    t=m+1
        temp = m
        while l<=r:
            m = l+(r-l)//2
            if matrix[temp][m]==target:
                return True
            else:
                if matrix[temp][m]>target:
                    r=m-1
                else:
                    l=m+1
            
        return False