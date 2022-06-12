class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l,r = 0,0
        n = len(nums)
        window = set()
        ans = 0
        maxDiff = 0
        
        
        @cache
        def sumTill(x):
            if x<0:
                return 0
            else:
                return nums[x]+sumTill(x-1)
            
        while r<n:
            if nums[r] not in window:
                window.add(nums[r])
                # maxDiff = r-l
                ans = max(ans,sumTill(r)-sumTill(l-1))
                r+=1
            else:
                window.remove(nums[l])
                l+=1
            
            
        
        return ans