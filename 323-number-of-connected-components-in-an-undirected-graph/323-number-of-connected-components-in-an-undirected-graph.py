class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        vis = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            vis.add(node)
            for dest in adj[node]:
                if dest not in vis:
                    dfs(dest)
            
        ans = 0
        for i in range(n):
            if i in vis:
                continue
            else:
                ans +=1
                dfs(i)
        
        return ans
                
        