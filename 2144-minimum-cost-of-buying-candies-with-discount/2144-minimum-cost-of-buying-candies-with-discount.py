class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)-1
        picked = 0
        ans = 0
        while n>=0:
            if picked==2:
                picked = 0
            else:
                ans+=cost[n]
                picked+=1
            n-=1
        return ans