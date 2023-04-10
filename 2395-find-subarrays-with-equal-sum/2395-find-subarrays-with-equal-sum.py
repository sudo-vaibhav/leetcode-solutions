class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        n = len(nums)
        seen = set()
        for start in range(n-1):
            
            nex = nums[start+1]
            s = nex+nums[start]
            if s in seen:
                return True
            seen.add(s)
        return False