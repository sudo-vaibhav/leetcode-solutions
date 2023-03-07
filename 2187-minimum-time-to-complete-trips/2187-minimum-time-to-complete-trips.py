class Solution:
    def minimumTime(self, time: List[int], tot: int) -> int:
        
        
        
        l,r = 0,max(time)*tot
        ans = r
        
        def compute(t):
            temp = 0
            
            for tim in time:
                temp += t//tim
            return temp>=tot
        
        while l<=r:
            m = (l+r)//2
            if compute(m):
                ans = m
                r = m-1
            else:
                l = m+1
        return ans