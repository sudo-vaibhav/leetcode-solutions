class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        l,r = 0,0
        
        while r<n:
            pool = []
            while r<n and colors[r]==colors[l]:
                heappush(pool,neededTime[r])
                r+=1
            
            while len(pool)>1:
                curPopped = heappop(pool)
                ans += curPopped
            
            l = r
        
        return ans
        