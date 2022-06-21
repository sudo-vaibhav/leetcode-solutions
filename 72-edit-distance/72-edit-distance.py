class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        @cache
        def solve(i,j):
            if i==m or j==n:
                return n-j+m-i
            if text1[i]==text2[j]:
                return solve(i+1,j+1)
            else:
                return 1+min(solve(i+1,j+1),solve(i,j+1),solve(i+1,j))
            
        return solve(0,0)