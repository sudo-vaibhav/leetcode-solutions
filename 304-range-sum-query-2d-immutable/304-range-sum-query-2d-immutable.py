class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        self.m = len(mat)
        self.n = len(mat[0])
        self.pSums = [[0] for _ in range(self.n)]
        
        for col in range(self.n):
            for row in range(self.m):
                self.pSums[col].append(mat[row][col]+self.pSums[col][-1])
    
    @cache
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for col in range(col1,col2+1):
            ans+=self.pSums[col][row2+1]-self.pSums[col][row1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)