class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        adj = [[] for i in range(N)]
        indegree = [0]*N
        for u,v in edges:
            adj[u].append(v)
            indegree[v]+=1
        explored = 0
        cols = [defaultdict(int) for _ in range(N)]
        distinct_cols = set(colors)
        ans = 0
        q = deque([i for i in range(N) if indegree[i]==0])
        while q:
            lenQ = len(q)    
            for _ in range(lenQ):
                explored+=1
                cur = q.popleft()
                cols[cur][colors[cur]]+=1
                ans = max(ans,cols[cur][colors[cur]])
                for dest in adj[cur]:
                    for col in distinct_cols:
                        cols[dest][col] = max(cols[dest][col],cols[cur][col])
                    indegree[dest]-=1
                    if indegree[dest]==0:
                        q.append(dest)
        
        return ans if explored==N else -1
        