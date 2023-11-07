class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ttr = sorted([d/s for d,s in zip(dist,speed)])
        ans = 0
        for i in range(len(ttr)):
            if ttr[i]<=i: break
            else: ans+=1
        return ans