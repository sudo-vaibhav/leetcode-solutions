class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def solve(start,end):
            if end<start: return 0
            if end==start: return 1
            if end-start==1: return 1 if s[start]==s[end] else 2
            ans = 1+solve(start+1,end)
            for k in range(start+1,end+1):
                if s[k]==s[start]:
                    ans = min(ans,solve(start,k-1)+solve(k+1,end))
            return ans
                
        
        return solve(0,len(s)-1)