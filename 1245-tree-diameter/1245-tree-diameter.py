class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        maxi = 0
        def solve(node):
            nonlocal maxi
            hp = [0]
            visited.add(node)
            for v in adj[node]:
                if v not in visited:
                    
                    hp.append(solve(v))
            hp = list(sorted(hp,reverse=True))[:2]
            ans = 1+sum(hp)
            visited.remove(node)
            maxi = max(maxi,ans)
            return 1+hp[0]
        
        solve(0)
        
        return maxi-1