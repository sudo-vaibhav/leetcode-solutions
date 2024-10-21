class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        
        def solve(i,seen):
            if i==len(s):
                return 0
            running = ""
            ans = 0
            for j in range(i,len(s)):
                running += s[j]
                if running not in seen:
                    seen.add(running)
                    ans = max(ans,1+solve(j+1,seen))
                    seen.remove(running)
            return ans
        return solve(0,set())