class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = [str(i) for i in range(1,n+2)]
        
        l,r = 0,0
        
        while r<n:
            while r<n and pattern[r]=="I":
                r+=1
            l = r
            while r<n and pattern[r]=="D":
                r+=1
            ans[l:r+1] = ans[l:r+1][::-1]
        
        return "".join(ans)