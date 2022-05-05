class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        n = len(mat)
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        for j in range(n//2):
            for i in range(n):
                mat[i][j],mat[i][n-1-j] = mat[i][n-1-j],mat[i][j]
                
        