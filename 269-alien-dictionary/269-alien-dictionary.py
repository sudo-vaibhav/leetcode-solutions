class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        n = len(words)
        chars = set()
        if len(words)==1: return "".join(set(words[0]))
        for i in range(n):
            for j in range(i+1,n):
                cur,nex = words[i],words[j]
                t = max(len(cur),len(nex))
                # found = False
                for j in range(t):
                    c1,c2 = None,None
                    if j<len(cur):
                        c1 = cur[j]
                        if c1 not in adj:
                            adj[c1] = set()

                    if j<len(nex):
                        c2 = nex[j]                    
                        if c2 not in adj:
                            adj[c2] = set()

                for j in range(t):
    #                 c1,c2 = None,None
    #                 if j<len(cur):
    #                     c1 = cur[j]
    #                     if c1 not in adj:
    #                         adj[c1] = set()

    #                 if j<len(nex):
    #                     c2 = nex[j]                    
    #                     if c2 not in adj:
    #                         adj[c2] = set()

                    if j<min(len(cur),len(nex)):
                        c1,c2 = cur[j],nex[j]
                        if c1!=c2:
                            if c1 in adj[c2]:
                                return ""
                            else:
                                adj[c1].add(c2)
                                # found = True
                                break
                else:
                    if len(cur)>len(nex): return ""
                # else:
                    
#             else:
#                 return ""
        
        def topo():
            seen = set()
            ans = []
            def dfs(node):
                seen.add(node)
                for dest in adj[node]:
                    if dest not in seen:
                        dfs(dest)
                ans.append(node)
                
            for c in adj:
                if c not in seen:
                    dfs(c)
            return ans
        return "".join(topo()[::-1])