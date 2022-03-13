class Solution:
    
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if(n==0): return -1
        if n==1:
            if k%2==1: return -1
            else: return nums[0]
        if k==0: return nums[0]
        if(k==1): 
            if n==1: return -1
            else: return nums[1]
        
        if k>n:
            return max(nums)
        elif k<n:
            return max(max(nums[:k-1]),nums[k])
        else:
            return max(nums[:k-1])