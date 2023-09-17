class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        ans = inf
        
        
        def findAns(start):
            q = deque([(start,1<<start)])
            seen = set(q)
            steps = 0
            
            while q:
                lenQ = len(q)
                
                for _ in range(lenQ):
                    
                    cur,seenSoFar = q.popleft()
                    # print(start,cur,seenSoFar)
                    if seenSoFar==(1<<n)-1:
                        return steps
                    for v in graph[cur]:
                        newSeen = seenSoFar|(1<<v)
                        if (v,newSeen) not in seen:
                            seen.add((v,newSeen))
                            q.append((v,newSeen))
                steps+=1
            return inf
            
        for start in range(n):
            ans = min(ans,findAns(start))
            
        # print(ans)
        return ans
            