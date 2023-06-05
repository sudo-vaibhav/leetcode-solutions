from fractions import Fraction
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        n = len(coordinates)
        
        # x,y = map(lambda x:x[0],coordinates),map(lambda y:y[1],coordinates)
        
        
        
        def getSlope(i,j):
            p1,p2 = coordinates[i],coordinates[j]
            sign = 1 if p2[1]-p1[1] >=0 else -1
            if p2[0]==p1[0]: return sign*inf
            #     return Fraction(sign*inf,1)
            # else:
            return Fraction(p2[1]-p1[1],p2[0]-p1[0])
            
        prev = getSlope(0,1)
        
        for i in range(2,n):
            s = getSlope(i-1,i)
            if s!=prev:
                return False
        return True
        