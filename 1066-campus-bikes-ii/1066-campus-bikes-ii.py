class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n,m = map(len,([workers,bikes]))
        
        def man(p1,p2):
            x1,y1,x2,y2 = *p1,*p2
            return abs(x1-x2)+abs(y1-y2)
        
        h = []
#         for i in range(n):
#             for j in range(m):
#                 heappush(h,(man(workers[i],bikes[j]),))
        @cache
        def solve(i,taken):
            if i==n:
                return 0
            else:
                ans = inf
                for j in range(m):
                    if not(taken&1<<j):
                        ans = min(ans,man(workers[i],bikes[j])+solve(i+1,taken|1<<j))
                return ans
        
        return solve(0,0)