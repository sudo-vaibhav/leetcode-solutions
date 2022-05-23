class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        v1 = nums[-1]*nums[-2]*nums[-3]
        v2 = nums[0]*nums[1]*nums[-1]
        
        return max(v1,v2)