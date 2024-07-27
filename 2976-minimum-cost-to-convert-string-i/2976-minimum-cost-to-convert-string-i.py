class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        
        adj = defaultdict(lambda : defaultdict(lambda :inf))
        for i,j,c in zip(original,changed,cost):
            adj[i][j] = min(adj[i][j],c)
        alphabets = [chr(ord('a')+i) for i in range(26)]
        # print(alphabets,adj)
        for k in alphabets:
            for i in alphabets:
                for j in alphabets:
                    adj[i][j] = min(adj[i][j],adj[i][k]+adj[k][j])
                    adj[j][i] = min(adj[j][i],adj[j][k]+adj[k][i])
        ans = 0
        for i in range(n):
            if source[i]!=target[i]:
                ans += adj[source[i]][target[i]]
        if ans==inf:
            return -1
        return ans
            
            
        