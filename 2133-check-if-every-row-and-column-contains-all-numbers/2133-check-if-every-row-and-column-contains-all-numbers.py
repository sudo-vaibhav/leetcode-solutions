class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        row = defaultdict(dict)
        col = defaultdict(dict)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                if(val in row[i]):
                    return False
                else:
                    row[i][val] = True
                if(val in col[j]):
                    return False
                else:
                    col[j][val] = True
        return True
                