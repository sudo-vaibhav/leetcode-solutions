class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for i in range(n)]
        
        for f in flights:
            adj[f[0]].append((f[1],f[2]))
          
        print(adj)
        
        @cache
        def solve(source,dest,k):
            if dest==source: return 0
            if k<0:return inf
            ans = inf
            for place,price in adj[source]:
                ans = min(ans,price+solve(place,dest,k-1))
            return ans
        
        s = solve(src,dst,k)
        return -1 if s==inf else s