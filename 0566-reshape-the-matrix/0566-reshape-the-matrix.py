class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        
        if m*n!=r*c:
            return mat
        
        ans = list(map(lambda x:[0]*c, range(r)))
        
        # print(ans)
        
        R,C = 0,0
        
        for i in range(m):
            for j in range(n):
                ans[R][C] = mat[i][j]
                C+=1
                if C==c:
                    R+=1
                    C=0
        
        return ans