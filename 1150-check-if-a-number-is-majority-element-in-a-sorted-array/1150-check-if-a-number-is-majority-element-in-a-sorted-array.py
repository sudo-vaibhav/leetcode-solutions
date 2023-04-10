class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        
        n = len(nums)
        return nums.count(target)>n//2