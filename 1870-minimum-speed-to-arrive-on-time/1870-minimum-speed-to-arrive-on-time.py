class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        
        l,r = 1,10**7
        ans = -1
        
        while l<=r:
            m = (l+r)//2
            # print(m)
            time = 0
            for idx,d in enumerate(dist):
                timetaken = d/m
                # print(timetaken,ceil(timetaken))
                time+=ceil(timetaken) if idx!=len(dist)-1 else timetaken
            if time<=hour:
                ans = m
                r = m-1
            else:
                l = m+1
        
        return ans
            