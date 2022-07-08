class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        
        l,r = 0,0
        ans = 1
        windowSum = 0
        
        
#       to make r as final elem
        def getCost(l,r,windowSum):
            ws = r-l
            cost = ws*nums[r] - windowSum 
            return cost
        
        while r<n:
            
            while getCost(l,r,windowSum)>k:
                windowSum -= nums[l]
                l+=1
                
            windowSum += nums[r]
            r+=1
            
            ans = max(ans,r-l)
        
        return ans