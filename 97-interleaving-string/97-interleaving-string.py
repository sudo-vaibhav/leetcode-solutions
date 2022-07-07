class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,p = len(s1),len(s2),len(s3)
        
        @cache
        def solve(i,k):
            j = k-i
            if k==p:
                return i==m and j==n and k==p
            ans = False
            if i<m and s1[i]==s3[k]:
                ans = ans or solve(i+1,k+1)
            if j<n and s2[j]==s3[k]:
                ans = ans or solve(i,k+1)
            return ans
        
        return solve(0,0)
        
        
        