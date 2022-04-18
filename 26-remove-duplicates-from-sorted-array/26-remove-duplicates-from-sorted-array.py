class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,0
        n = len(nums)
        if [nums[0]]*n==nums: return 1
        while r<n:
            while r<n and nums[r-1]==nums[r]:
                r+=1
            # k+=1
            if r<n:
                nums[l] = nums[r]
                l+=1
            r+=1
                
        
        return l