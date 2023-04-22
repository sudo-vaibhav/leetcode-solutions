class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        
        @cache
        def solve(i,j):
            # print(i,j)
            if i>=j: return 0
            I,J = s[i],s[j]
            
            if I==J:
                return solve(i+1,j-1)
            else:
                return 1+min(solve(i,j-1),solve(i+1,j))
        
        return solve(0,n-1)