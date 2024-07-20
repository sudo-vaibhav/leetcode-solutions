class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        m,n = map(len,[rowSum,colSum])
        ans = [[None]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp = min(colSum[j],rowSum[i])
                ans[i][j] = temp
                rowSum[i]-=temp
                colSum[j]-=temp
        return ans
                