class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n = len(points),len(points[0])
        prevRow = points[0]
        
        for r in range(1,m):
            leftMax = [0]*n
            rightMax = [0]*n
            
            leftMax[0] = prevRow[0]
            rightMax[-1]=prevRow[-1]
            ans = 0
            for c in range(1,n):
                leftMax[c] = max(leftMax[c-1]-1,prevRow[c])
                
            for c in range(n-2,-1,-1):
                rightMax[c] = max(rightMax[c+1]-1,prevRow[c])
            cR = [0]*n
            for c in range(n):
                cR[c] = points[r][c]+max(leftMax[c],rightMax[c])
            prevRow = cR
        
        return max(prevRow)