class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        gph = defaultdict(list)
        for u,v in connections:
            gph[u].append((v,True))
            gph[v].append((u,False))
        
        def solve(node,prev=-1):
            ans = 0
            for nex,dn in gph[node]:
                if nex!=prev:
                    ans += dn==True
                    ans+=solve(nex,node)
            return ans
        
        return solve(0)
    
    
    
    
    