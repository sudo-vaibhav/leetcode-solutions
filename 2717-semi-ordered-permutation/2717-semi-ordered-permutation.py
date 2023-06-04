class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        one,last = nums.index(1),nums.index(len(nums))
        
        return one+(len(nums)-last-1)-(one>last)