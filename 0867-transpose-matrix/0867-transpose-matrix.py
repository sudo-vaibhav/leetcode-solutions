class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = map(len,[matrix,matrix[0]])
        newmat = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                newmat[j][i]=matrix[i][j]
        return newmat
                