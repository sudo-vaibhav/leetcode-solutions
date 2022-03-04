class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = [-1,-1]
        
        
        # find lower rn
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                ans[0] = mid
                r = mid-1
                
        # find for higher now
        l ,r = 0,len(nums)-1
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                ans[1] = mid
                l = mid+1
                
        return ans
                
