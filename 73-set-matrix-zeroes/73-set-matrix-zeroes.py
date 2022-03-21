class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for l in range(n):
                        if matrix[i][l] != 0:
                            matrix[i][l] = float("inf")
                    for l in range(m):
                        if matrix[l][j] !=0:
                            matrix[l][j] = float("inf")
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==float("inf"):
                    matrix[i][j] = 0
        
                
        