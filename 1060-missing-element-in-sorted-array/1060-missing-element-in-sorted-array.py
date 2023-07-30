class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l,r = 0,len(nums)-1
        base = min(nums)
        
        while l<r:
            m = r-(r-l)//2
            expected = base+m
            missing = nums[m]-expected
            if missing>=k:
                r = m-1
            else:
                l = m
        
        return base+k+l