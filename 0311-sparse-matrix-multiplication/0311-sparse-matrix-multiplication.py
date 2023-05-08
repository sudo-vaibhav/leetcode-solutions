class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m,n,o = len(mat1),len(mat1[0]),len(mat2[0])
        ans = [[0]*o for _ in range(m)]
        for i in range(m):
            for j in range(o):
                temp = 0
                for k in range(n):
                    temp += mat1[i][k]*mat2[k][j]
                ans[i][j]=temp
        return ans