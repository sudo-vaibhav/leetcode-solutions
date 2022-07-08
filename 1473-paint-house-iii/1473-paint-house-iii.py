class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        houseCnt = len(houses)
        # cost[house][color+1]
        @cache
        def solve(i,prev,grpSoFar):
            if i==houseCnt:
                if grpSoFar==target:
                    return 0
                else:
                    return inf
            if grpSoFar>target:
                return inf
            curCol = houses[i]
            
            if curCol!=0:
                return solve(i+1,curCol,grpSoFar + (1 if curCol!=prev else 0))
            else:
                ans = inf
                for curCol in range(1,n+1):
                    ans = min(ans, cost[i][curCol-1] + solve(i+1,curCol,grpSoFar + (1 if curCol!=prev else 0)))
                return ans
        
        res = solve(0,inf,0)
        return res if res!=inf else -1