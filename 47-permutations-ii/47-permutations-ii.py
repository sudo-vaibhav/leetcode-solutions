class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def solve(idx):
            if idx==n:
                ans.append(tuple(nums))
            else:
                done = set()
                for i in range(idx,n):
                    if nums[i] not in done:
                        nums[idx],nums[i] = nums[i],nums[idx]
                        solve(idx+1)
                        nums[idx],nums[i] = nums[i],nums[idx]
                        done.add(nums[i])
        solve(0)
        return ans