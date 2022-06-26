class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        n,tot = len(cp),sum(cp)
        k = n-k
        running = 0
        ans = inf
        if k==0:return tot
        for r in range(n):
            running += cp[r]
            if r>=k-1:
                ans = min(ans,running)
                running -= cp[r-k+1]
        return tot-ans
            