class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degrees = defaultdict(int)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degrees[u]+=1
            degrees[v]+=1
        if n==0:
            return []
        if n==1:
            return [0]
        
        q = deque()
        for i in range(n):
            if degrees[i]==1:
                q.append(i)
        totalNodes = n   
        # self.lastIterQ = []
        while totalNodes>2:
            qsize = len(q)
            totalNodes -= qsize
            for _ in range(qsize):
                cur = q.popleft()
                for dest in adj[cur]:
                    degrees[dest]-=1
                    if degrees[dest]==1:
                        q.append(dest)
        return q
        