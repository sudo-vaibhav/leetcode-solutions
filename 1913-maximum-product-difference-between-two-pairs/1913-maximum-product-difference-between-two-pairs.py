class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        c,d,*v,a,b=sorted(nums)
        
        return a*b-c*d