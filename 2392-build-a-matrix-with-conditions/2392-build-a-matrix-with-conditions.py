class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def getOrdering(conds):
            adj = defaultdict(list)
            indegree = defaultdict(int)
            for u,v in conds:
                adj[u].append(v)
                indegree[v]+=1
            q = deque()
            for i in range(1,k+1):
                if indegree[i]==0: q.append(i)
            ans = list(q)
            while q:
                lenQ = len(q)
                for _ in range(lenQ):
                    cur = q.popleft()
                    for v in adj[cur]:
                        indegree[v]-=1
                        if indegree[v]==0:
                            ans.append(v)
                            q.append(v)
            return ans
                    
        rows = getOrdering(rowConditions)
        cols = getOrdering(colConditions)

        if len(rows)<k or len(cols)<k:
            return []

        indices = defaultdict(lambda : [None,None])
        for i in range(k):
            indices[rows[i]][0] = i
        for j in range(k):
            indices[cols[j]][1] = j
        ans = [[0]*k for _ in range(k)]
        for i,(u,v) in indices.items():
            ans[u][v] = i
        return ans