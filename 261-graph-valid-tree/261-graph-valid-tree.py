class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        vis = set()
        
        adj = defaultdict(list)
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        def dfs(node,parent):
            for v in adj[node]:
                if v in vis:
                    if v!=parent:
                        return False
                    else:
                        continue
                else:
                    vis.add(v)
                    if not dfs(v,node):
                        return False
            return True
            
        vis.add(0)          
        return dfs(0,-1) and len(vis)==n