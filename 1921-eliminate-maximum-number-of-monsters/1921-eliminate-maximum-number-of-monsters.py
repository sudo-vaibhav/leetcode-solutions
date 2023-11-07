class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        ttr = [d/s for d,s in zip(dist,speed)]
        ttr.sort()
        ans = 0
        
        prevDefeated = -inf
        # time = 0
        for i in range(len(ttr)):
            if ttr[i]<=i:
                break
            else:
                ans+=1
                
        # print(ttr)
        return ans