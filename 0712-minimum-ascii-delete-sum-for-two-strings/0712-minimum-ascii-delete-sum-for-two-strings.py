class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = map(len,[s1,s2])
        @cache
        def beyond(s,p):
            if p==len(s):return 0
            return ord(s[p])+beyond(s,p+1)
            
        @cache
        def solve(i,j):
            if i==m or j==n:
                if i!=m:
                    return beyond(s1,i)
                if j!=n:
                    return beyond(s2,j)
                return 0
            else:
                if s1[i]==s2[j]:
                    return solve(i+1,j+1)
                else:
                    return min(ord(s1[i])+solve(i+1,j),ord(s2[j])+solve(i,j+1))
            
        ans = solve(0,0)
               
        return ans