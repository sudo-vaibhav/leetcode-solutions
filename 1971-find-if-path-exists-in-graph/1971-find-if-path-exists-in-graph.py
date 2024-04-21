class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        def dfs(node,seen=set()):
            if node==destination:
                return True
            for nex in adj[node]:
                if nex not in seen:
                    seen.add(nex)
                    if dfs(nex,seen):
                        return True
            return False
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return dfs(source)
        