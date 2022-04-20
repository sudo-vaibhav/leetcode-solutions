class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans,n = 1,len(points)
        points.sort()
        
        def getOlap(l,r):
            # l = cur if cur[0]<olapIvl[0] else olapIvl
            # r = cur if l!=cur else olapIvl
            overlap = [max(l[0],r[0]),min(l[1],r[1])]
            if overlap[0]>overlap[1]:
                return False
            return overlap
            
        olapIvl = points[0]
        
        for idx in range(1,n):
            cur = points[idx]
            temp = getOlap(cur,olapIvl)
            if temp==False:
                ans+=1
                olapIvl = cur
            else:
                olapIvl = temp
        return ans
            
        