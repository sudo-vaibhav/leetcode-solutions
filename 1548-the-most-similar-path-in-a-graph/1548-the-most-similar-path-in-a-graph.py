class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        # at node , till index idx of target path, whats the best edit distance we can give
        # dp[node][idx]
        dp = defaultdict(lambda : defaultdict(lambda:inf))
        
        adj = defaultdict(list)
        
        for u,v in roads:
            adj[u].append(v)
            adj[v].append(u)
        
        for node in range(n):
            dp[node][0]=1 if names[node]!=targetPath[0] else 0
            
        for idx in range(1,len(targetPath)):
            for node in range(0,n):
                for v in adj[node]:
                    dp[node][idx]=min(dp[node][idx],int(targetPath[idx]!=names[node])+dp[v][idx-1])
        
        
        
        minDiff = min(dp[node][len(targetPath)-1] for node in range(n))
        ans = []
        # print(minDiff,dp)
        def solve(node,idx):
            # print("running")
            diff = dp[node][idx]
            newDiff = diff-int(names[node]!=targetPath[idx])
            ans.append(node)
            for v in adj[node]:
                if dp[v][idx-1]==newDiff:
                    solve(v,idx-1)
                    break
                    
        for i in range(n):
            if dp[i][len(targetPath)-1]==minDiff:
                solve(i,len(targetPath)-1)
                break
        
        return reversed(ans)