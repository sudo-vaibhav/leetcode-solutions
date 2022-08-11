class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        X,Y = location
        def getTransformedPoint(x,y):
            dx,dy = x-X,y-Y
            if dx==0 and dy==0:
                return True
            else:
                return math.degrees(math.atan2(dy,dx))+180
        base = 0
        thetas = []
        for pt in points:
            theta = getTransformedPoint(*pt)
            if theta==True:
                base += 1
            else:
                thetas.append(theta)
        n = len(thetas)
        thetas.sort()
        for i in range(n):
            thetas.append(thetas[i]+360)
        
        l,r = 0,0
        n*=2
        inrange = 0
        maxinrange = 0
        while r<n:
            while l<n and thetas[r]-thetas[l]>angle:
                l+=1
            r+=1
            maxinrange = max(maxinrange,r-l)
        
        return maxinrange+base
            
            
                
            