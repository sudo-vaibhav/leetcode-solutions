class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = defaultdict(int)
        l =0
        ans = 0
        for r in range(n):
            
            c[nums[r]]+=1
            
            while l<=r and c[nums[r]]>k:
                c[nums[l]]-=1
                l+=1
            ans = max(ans,r-l+1)
        return ans