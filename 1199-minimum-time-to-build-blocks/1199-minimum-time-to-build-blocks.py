class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        blocks.sort(reverse=True)
        n = len(blocks)
        
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        
        def solve(i,workers):
            if i==n: return 0
            if workers==0:return inf
            if workers>=n-i:return blocks[i]
            if dp[i][workers]!=-1:return dp[i][workers]
            dp[i][workers]=min(
                split+solve(i,min(2*workers,n-i)), 
                max(blocks[i],solve(i+1,workers-1))
            )
            return dp[i][workers]
        return solve(0,1)