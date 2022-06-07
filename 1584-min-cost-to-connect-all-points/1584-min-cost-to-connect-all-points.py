class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        distances = [inf for _ in points]
        distances[0] = 0
        parent = [-1 for _ in points]
        pq = [(0,0)]
        @cache
        def getDist(i1,i2):
            p1,p2 = points[i1],points[i2]
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        while len(visited)<len(points):
            dist,pIdx = heappop(pq)
            if pIdx in visited:
                continue
            visited.add(pIdx)
            point = points[pIdx]
            
            for i in range(len(points)):
                if i not in visited:
                    temp = getDist(pIdx,i) 
                    if temp<distances[i]:
                        distances[i] = temp
                        heappush(pq,(temp,i))
                        parent[i] = pIdx
        ans = 0
        for i in range(len(points)):
            if parent[i]!=-1:
                ans+=getDist(i,parent[i])
        return ans
                        
                    
            
        
        