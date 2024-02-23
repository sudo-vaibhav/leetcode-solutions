class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        
        for s,d,c in flights:
            adj[s].append((d,c))
            
        ans = inf
        
        @cache
        def solve(i,k):
            if i==dst:
                return 0
            if k==-1:
                return inf
            sol = inf
            for v,c in adj[i]:
                temp = solve(v,k-1)
                sol = min(sol,temp+c)
            return sol
                    
        
        ans = solve(src,k)
        return ans if ans!=inf else -1
        