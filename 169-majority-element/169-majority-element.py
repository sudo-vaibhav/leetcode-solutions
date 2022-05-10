class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 1
        
        for i in range(1,len(nums)):
            cur = nums[i]
            if count==0:
                ans = cur
            if ans==cur:
                count+=1
            else:
                count-=1
        return ans