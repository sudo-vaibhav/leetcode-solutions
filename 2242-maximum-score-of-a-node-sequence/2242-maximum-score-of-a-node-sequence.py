class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        adj,ans = defaultdict(list),-1
        for u,v in edges:
            adj[u].append((scores[v],v))
            adj[v].append((scores[u],u))
        for i in adj:
            adj[i] = nlargest(3,adj[i])
        for b,c in edges:
            for (aW,a),(dW,d) in product(adj[b],adj[c]):
                if a!=c and d!=b and a!=d:
                    ans = max(ans,aW+dW+scores[b]+scores[c])
        return ans
        
        