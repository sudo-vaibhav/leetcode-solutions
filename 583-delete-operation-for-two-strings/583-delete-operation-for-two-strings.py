class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        m,n = len(w1),len(w2)
        @cache
        def lcs(i,j):
            if i<0 or j<0:return 0
            ans = lcs(i-1,j)
            ans = max(ans,lcs(i,j-1))
            if w1[i]==w2[j]:
                ans = max(ans,1+lcs(i-1,j-1))
            return ans
                
        
        temp = lcs(m-1,n-1)
        
        return (m+n)-2*temp