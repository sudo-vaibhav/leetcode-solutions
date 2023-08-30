class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n  = len(nums)
        ans = 0
        for i in range(n-2,-1,-1):
            cur = nums[i]
            nex=nums[i+1]
            temp = 0
            if cur>nex:
                num_el=ceil(cur/nex)
                nums[i]=cur//(num_el)
                ans += num_el-1
        return ans
            