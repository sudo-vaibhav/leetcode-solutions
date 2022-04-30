class Solution:
    def calcEquation(self, eqns, values, qrys):
        adj,ans= defaultdict(list),[]
        for idx,(u,v) in enumerate(eqns):
            val = values[idx]
            adj[u].append((v,val)),adj[v].append((u,1/val))
        def dfs(cur,target,vis,soFar=1.0):
            if cur==target and cur in adj:
                return soFar
            vis.add(cur)
            for dest,amt in adj[cur]:
                if dest not in vis:
                    temp= dfs(dest, target,vis,soFar*amt)
                    if temp!=-1.0:
                        return temp
            return -1.0
        for num,denom in qrys:
            vis = set()
            ans.append(dfs(num,denom,vis))
        return ans
            