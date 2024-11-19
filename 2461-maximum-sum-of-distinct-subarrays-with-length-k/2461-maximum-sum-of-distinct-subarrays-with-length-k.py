class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        c = defaultdict(int)
        s = 0
        ans = 0
        for i in range(len(nums)):
            # print(nums,i,s,c)
            if i>=k:
                c[nums[i-k]]-=1
                if c[nums[i-k]]==0:
                    del c[nums[i-k]]
                s-=nums[i-k]
            c[nums[i]]+=1
            s+=nums[i]
            if len(c)==k:
                ans = max(ans,s)
        return ans