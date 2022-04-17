class Solution:
    def longestPath(self, nodes: List[int], s: str) -> int:
        adj = defaultdict(list)
        
        for child,parent in enumerate(nodes):
            if parent!=-1:
                adj[parent].append(child)
        
        self.ans = -inf
        def dfs(node):
            lengths = []
            for child in adj[node]:
                t = dfs(child)
                if s[child]!=s[node]:
                    lengths.append(t)
            
            cur = 1+sum(nlargest(2,lengths) if len(lengths)>0 else [0])
            self.ans = max(self.ans,cur)
            return 1+max(nlargest(1,lengths) if len(lengths)>0 else [0])
            
        dfs(0)
        # print(adj)
        return self.ans
        