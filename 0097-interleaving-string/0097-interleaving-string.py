class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,p = map(len,[s1,s2,s3])
        @cache
        def solve(i,j,k):
            if k==p:
                return i==m and j==n
            else:
                ans = False
                if i<m and s1[i]==s3[k]:
                    ans|=solve(i+1,j,k+1)
                if j<n and s2[j]==s3[k]:
                    ans|=solve(i,j+1,k+1)
                return ans
        
        return solve(0,0,0)