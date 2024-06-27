class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in adj:
            if len(adj[i])>1:
                return i
            