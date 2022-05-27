class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        vis = set()
        
        adj = defaultdict(list)
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # print(adj)
        ans = True
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
        temp = dfs(0,-1)
        return temp and len(vis)==n