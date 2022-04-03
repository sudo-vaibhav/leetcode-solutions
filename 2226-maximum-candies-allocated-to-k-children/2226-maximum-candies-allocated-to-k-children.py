class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        totCand = sum(candies)
        if totCand<k:
            return 0
        else:
            def isPos(candCount):
                kidsSatisfied = 0
                for cand in candies:
                    kidsSatisfied+= cand//candCount
                return kidsSatisfied
            if totCand == k: return 1
            else:
                l = 1
                r = max(candies)
                ans = 1
                while l<=r:
                    m = l+(r-l)//2
                    
                    if isPos(m)>=k:
                        ans = max(ans,m)
                        l = m+1
                    else:
                        r= m-1
                return ans
                