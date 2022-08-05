class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # ans = 0
        
        @cache
        def solve(target):
            # nonlocal ans
            if target==0:
                # ans+=1
                return 1
            # if i==n:
            #     return 0
            temp = 0
            for i in range(n):
                if nums[i]<=target:
                    temp+=solve(target-nums[i])
            return temp
        return solve(target)
        # return ans