class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        vis,adj,ans = set(),defaultdict(list),list(s)
        
        def dfs(node):
            component.append((s[node]))
            positions.append(node)
            vis.add(node)
            for i in adj[node]:
                if i not in vis:
                    dfs(i)
                    
        for u,v in pairs:
            adj[u].append(v)
            adj[v].append(u)
            
        for i in range(len(s)):
            if i not in vis:
                component,positions = [],[]
                dfs(i)
                component.sort(),positions.sort()
                
                for idx,pos in enumerate(positions):
                    ans[pos]=component[idx]
        
        return "".join(ans)