class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1,n2 = map(len,[word1,word2])
        @cache
        def solve(i,j):
            if j==n2:
                return n1-i-1
            if i==n1:
                return n2-j-1
            ans = inf
            if word1[i]==word2[j]:
                ans = solve(i+1,j+1)
            else:
                ans = min(ans,1+min(solve(i+1,j+1),solve(i+1,j),solve(i,j+1)))
            
            return ans
        
        return solve(0,0)+1