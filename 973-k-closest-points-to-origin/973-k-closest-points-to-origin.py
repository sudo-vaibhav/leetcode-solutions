class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getNegDist(point):
            x,y = point
            return -(((x**2)+(y**2))**0.5)
        q = []
        for point in points:
            heappush(q,(getNegDist(point),point))
            if len(q)>k:
                heappop(q)
        return [p[1] for p in q]