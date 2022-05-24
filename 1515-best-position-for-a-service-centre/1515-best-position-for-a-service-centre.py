class Solution(object):
    def getMinDistSum(self, points):
        eps = 10**(-6)
        
        def getDist(x,y):
            res = 0
            for u,v in points:
                dx,dy = u-x,v-y
                res += ( dx**2 + dy**2 )**0.5
            return res
        
        def getOptimalDist(x):
            ly,ry = 0,100
            while ry-ly>eps:
                deltaY = (ry-ly)/3
                m1y,m2y = ly+deltaY,ry-deltaY
                d1,d2 = getDist(x,m1y),getDist(x,m2y)
                if d1<d2:
                    ry = m2y
                else : #d1>d2:
                    ly = m1y
                # else:
                #     ly = m1y
                #     ry = m2y
            # print("got y",ly)
            return getDist(x,ly)
        
        def getXY(points):
            lx,rx = 0,100
            while rx-lx>eps:
                deltaX = (rx-lx)/3
                m1x, m2x = lx+deltaX, rx-deltaX
                optimalDist1,optimalDist2 = getOptimalDist(m1x),getOptimalDist(m2x)
                if optimalDist1<optimalDist2:
                    rx = m2x
                else:# optimalDist1>optimalDist2:
                    lx = m1x
                # else:
                #     lx = m1x
                #     rx = m2x
            # print("got x",lx)
            return getOptimalDist(lx)
        
        # print("val check",getDist(0.99999999999,0.999999999999))
        return getXY(points)
