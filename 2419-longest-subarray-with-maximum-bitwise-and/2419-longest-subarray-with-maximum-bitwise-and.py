class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        a = max(nums)
        
        c = int(nums[0]==a)
        ans = 1
        
        for i in range(1,len(nums)):
            if nums[i]==a:
                c+=1
                ans = max(ans,c)
            else:
                c=0
        return ans
        