class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        visited = [False for i in range(n)]
        adj = defaultdict(list)
        x = defaultdict(set)
        def dfs(node):
            for dest in adj[node]:
                if not visited[dest]:
                    visited[dest]=True
                    dfs(dest)
                x[node] = x[node].union(x[dest])
            x[node].add(node)
            
        for edge in edges:
            u,v = edge
            adj[u].append(v)
            
        for i in range(n):
            if not visited[i]:
                dfs(i)
        # print(x)
        res = [set() for i in range(n)]
        for k in x.keys():
            for b in x[k]:
                if b!=k:
                    res[b].add(k)
        # print(res)
        return [sorted(list(r)) for r in res]
        
        