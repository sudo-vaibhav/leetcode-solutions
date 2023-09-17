class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        ans = inf
        q = deque()
        for start in range(n):
            q.append((start,1<<start))
            
        seen = set(q)
        steps = 0
            
        while q:
            lenQ = len(q)

            for _ in range(lenQ):

                cur,seenSoFar = q.popleft()
                if seenSoFar==(1<<n)-1:
                    return steps
                for v in graph[cur]:
                    newSeen = seenSoFar|(1<<v)
                    if (v,newSeen) not in seen:
                        seen.add((v,newSeen))
                        q.append((v,newSeen))
            steps+=1
        # print(ans)
            