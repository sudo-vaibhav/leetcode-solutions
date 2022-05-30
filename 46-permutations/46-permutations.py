class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)
        def solve(idx):
            if idx==N:
                ans.append(list(nums))
            else:
                for i in range(idx,N):
                    nums[i],nums[idx]=nums[idx],nums[i]
                    solve(idx+1)
                    nums[i],nums[idx]=nums[idx],nums[i]
                    
        
        solve(0)
        return ans