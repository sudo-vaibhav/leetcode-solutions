class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            if(n%2!=1 or i != n//2):
                ans += mat[i][i]
            
            ans += mat[n-i-1][i]
        
        return ans