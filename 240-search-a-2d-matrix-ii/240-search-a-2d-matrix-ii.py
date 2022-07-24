class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m,n = len(mat),len(mat[0])
        
        for i in range(m):
            cur = mat[i]
            
            idx = bisect_left(cur,target)
            if 0<=idx<n and cur[idx]==target:
                return True
        
        return False