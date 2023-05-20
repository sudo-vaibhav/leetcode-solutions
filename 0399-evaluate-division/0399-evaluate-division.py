class Solution:
    def calcEquation(self, eqs: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        adj = defaultdict(set)
        
        for i in range(len(values)):
            # adj[eqs[i][0]].add((eqs[i][0],1))
            # adj[eqs[i][1]].add((eqs[i][1],1))
            adj[eqs[i][0]].add((eqs[i][1],values[i]))
            adj[eqs[i][1]].add((eqs[i][0],1/values[i]))
        
        seen = set()
        res = []
        for init,target in queries:
            ans = []
            def solve(node,cur):
                if node==target: ans.append(cur)      
                else:
                    for v,mult in adj[node]:
                        if v not in seen:                              
                            seen.add(v)
                            solve(v,cur*mult)
                            seen.remove(v)
            if init not in adj or target not in adj: res.append(-1)
            else:
                solve(init,1)
                if len(set(ans))==1:
                    res.append(ans[0])
                else:
                    res.append(-1)

        return res
                        
                
            