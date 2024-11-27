class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(n-1):
            adj[i].append(i+1)
        ans = []
        
            
        for u,v in queries:
            adj[u].append(v)
            @cache
            def solve(i):
                if i==n-1:
                    return 0
                ans = inf
                for v in adj[i]:
                    ans = min(ans,solve(v)+1)
                return ans
            ans.append(solve(0))
        return ans
        
            