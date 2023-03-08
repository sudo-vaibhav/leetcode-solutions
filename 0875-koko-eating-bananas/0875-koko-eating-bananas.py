class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        l,r = 1,sum(piles)
        ans = r
        
        def pos(m):
            ans = 0
            for b in piles:
                ans += ceil(b/m)
            return ans<=h
        
        while l<=r:
            m = (l+r)//2
            
            if pos(m):
                ans = m
                r = m-1
            else:
                l = m+1
            
        return ans