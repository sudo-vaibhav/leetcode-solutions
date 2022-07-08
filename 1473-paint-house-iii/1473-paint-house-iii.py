class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        houseCnt = len(houses)
        @cache
        def solve(idx,prev,grpSoFar):
            if grpSoFar>target or idx==houseCnt:
                if grpSoFar==target:
                    return 0
                else:
                    return inf
            curCol = houses[idx]
            if curCol!=0:
                return solve(idx+1,curCol,grpSoFar + (1 if curCol!=prev else 0))
            else:
                ans = inf
                for curCol in range(1,n+1):
                    ans = min(ans, cost[idx][curCol-1] + solve(idx+1,curCol,grpSoFar + (1 if curCol!=prev else 0)))
                return ans
        
        res = solve(0,inf,0)
        return res if res!=inf else -1