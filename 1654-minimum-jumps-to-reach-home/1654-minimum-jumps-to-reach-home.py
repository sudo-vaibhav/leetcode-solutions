class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        vis = set()
        @cache
        def minJumps(src,dest,forJump,backJump,canJumpBack):
            vis.add((src,canJumpBack))
            if dest==src: return 0
            if ((src<0) or (src in forbidden) or (src>6000)): return inf
            tempans = inf
            if (src+forJump,1) not in vis:
                tempans = 1+minJumps(src+forJump,dest,forJump,backJump,1)
            if canJumpBack==1 and (src-backJump,0) not in vis:
                tempans = min(tempans,1+minJumps(src-backJump,dest,forJump,backJump,0))
            return tempans
        t = minJumps(0,x,a,b,1)
        return t if t!=inf else -1 
        
        