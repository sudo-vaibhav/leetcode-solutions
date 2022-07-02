class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0,h])
        verticalCuts.extend([0,w])
        horizontalCuts.sort()
        verticalCuts.sort()
        MOD = 10**9+7
        maxDiffHoriz,maxDiffVert = 0,0
        for i in range(len(horizontalCuts)-1):
            maxDiffHoriz = max(maxDiffHoriz,horizontalCuts[i+1] - horizontalCuts[i])
            
        for i in range(len(verticalCuts)-1):
            maxDiffVert = max(maxDiffVert,verticalCuts[i+1] - verticalCuts[i])
        
        return (maxDiffVert*maxDiffHoriz)%MOD
            
        