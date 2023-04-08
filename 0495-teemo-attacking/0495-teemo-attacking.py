class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        ans = 0
        ptill = 0
        for p in timeSeries:
            
            ans+= duration-max(0,ptill-p)
            ptill = p+duration
        return ans