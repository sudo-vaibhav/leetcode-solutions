class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m,n = len(mat),len(mat[0])
        
#         for i in range(m):
#             cur = mat[i]
            
#             idx = bisect_left(cur,target)
#             if 0<=idx<n and cur[idx]==target:
#                 return True
        
#         return False

        i,j = m-1,0
    
        while j<n and i>=0:
            cur = mat[i][j]
            
            if cur<target:
                j+=1
            elif cur>target:
                i-=1
            else:
                return True
        
        return False