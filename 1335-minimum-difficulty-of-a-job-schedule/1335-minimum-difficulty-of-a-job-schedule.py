class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)
        if d>n: return -1
        @cache
        def solve(i,d):
            if i==n or d==0:
                if i==n and d==0:
                    return 0
                return inf
            maxSeen = jobs[i]
            ans = maxSeen+solve(i+1,d-1)
            for curEnd in range(i+1,n):
                maxSeen = max(maxSeen,jobs[curEnd])
                ans = min(ans,maxSeen+solve(curEnd+1,d-1))
            return ans
        
        return solve(0,d)
                