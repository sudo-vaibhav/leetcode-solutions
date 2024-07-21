class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        
        # [1,3]->2 row ordering
        # 3->2->1
        # 0,0 -> 3
        # 1,1 -> 
        
        def getOrdering(conds):
            
            adj = defaultdict(list)
            indegree = defaultdict(int)
            for u,v in conds:
                adj[u].append(v)
                indegree[v]+=1
            q = deque()
            for i in range(1,k+1):
                if indegree[i]==0:
                    q.append(i)
            # print(q)
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
            # print(q,ans)
            if len(ans)<k:
                return []
            return ans
                    
        rows = getOrdering(rowConditions)
        cols = getOrdering(colConditions)
        # print(rows,cols)
        if len(rows)==0 or len(cols)==0:
            return []
        indices = defaultdict(list)
        for i in range(k):
            indices[rows[i]].append(i)
        for j in range(k):
            indices[cols[j]].append(j)
        ans = [[0]*k for _ in range(k)]
        for i,(u,v) in indices.items():
            ans[u][v] = i
        return ans