class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        def solve(idx):
            if idx==n:
                ans.add(tuple(nums))
            else:
                for i in range(idx,n):
                    nums[idx],nums[i] = nums[i],nums[idx]
                    solve(idx+1)
                    nums[idx],nums[i] = nums[i],nums[idx]
        solve(0)
        return ans