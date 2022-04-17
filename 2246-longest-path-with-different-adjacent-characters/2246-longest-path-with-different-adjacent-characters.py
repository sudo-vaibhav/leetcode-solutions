class Solution:
    def longestPath(self, nodes: List[int], s: str) -> int:
        adj,self.ans = defaultdict(list),-inf
        for child,parent in enumerate(nodes):
            if parent!=-1: adj[parent].append(child)
        def dfs(node):
            lengths = []
            for child in adj[node]:
                temp = dfs(child)
                if s[child]!=s[node]:
                    lengths.append(temp)
            cur = 1+sum(nlargest(2,lengths) if len(lengths)>0 else [0])
            if cur>self.ans: self.ans = cur
            return 1+(max(lengths) if len(lengths)>0 else 0)
        
        dfs(0)
        return self.ans
        