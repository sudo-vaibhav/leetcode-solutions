class Solution:
    def topo(self,chars,adj):
        seen = set()
        ans = []
        def dfs(node):
            seen.add(node)
            for dest in adj[node]:
                if dest not in seen:
                    dfs(dest)
            ans.append(node)

        for char in chars:
            if char not in seen:
                dfs(char)
        return "".join(ans[::-1])
    
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        chars = set()
        
        for word in words:
            for char in word:
                chars.add(char)
                
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                cur,nex = words[i],words[j]
                for it in range(min(len(cur),len(nex))):
                    c1,c2 = cur[it],nex[it]
                    if c1!=c2:
                        if c1 in adj[c2]:
                            return ""
                        else:
                            if c2 not in adj[c1]:
                                adj[c1].append(c2)
                            break
                else:
                    if len(cur)>len(nex): return ""
        
        return self.topo(chars,adj)