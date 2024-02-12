class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cur,count = nums[0],1
        
        for i in nums[1:]:
            if cur!=i:
                count-=1
            else:
                count+=1
            if count==0:
                count=1
                cur = i
        
        return cur