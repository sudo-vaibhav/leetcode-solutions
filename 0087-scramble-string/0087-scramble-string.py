class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if sorted(s1)!=sorted(s2): return False
        @cache
        def solve(i,j,p,q):
            if j-i!=q-p: return False
            if i==j: return s1[i]==s2[p]
            if not sorted(s1[i:j+1])==sorted(s2[p:q+1]): return False
            
            for k in range(j-i):
                if (solve(i,i+k,p,p+k) and solve(i+k+1,j,p+k+1,q)) or (solve(i,i+k,q-k,q) and solve(i+k+1,j,p,q-k-1)):
                    return True
            
            
            
            
#             for k in range(j-i):
#                 if (solve(i,i+k,p,p+k) and solve(i+k+1,j,p+k+1,q)) or (solve(i+k+1,j,p,p+k) and solve(i,i+k,p+k+1,q)):return True
            
            return False
                
        
        return solve(0,n-1,0,n-1)