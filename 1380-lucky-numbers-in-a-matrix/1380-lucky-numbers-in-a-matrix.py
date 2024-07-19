class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        def col(j):
            ans = []
            for i in range(len(matrix)):
                ans.append(matrix[i][j])
            return ans
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==min(matrix[i])==max(col(j)):
                    ans.append(matrix[i][j])
        return ans