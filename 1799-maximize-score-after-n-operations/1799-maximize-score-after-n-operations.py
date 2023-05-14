class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        n = len(nums)//2
        
        # steps = 0
        @cache
        def solve(steps,taken):
            # nonlocal steps
            if steps==n: return 0
            # steps+=1
            ans = 0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if (taken&1<<i)|(taken&1<<j):
                        continue
                    ans = max(ans,(steps+1)*gcd(nums[i],nums[j])+solve(steps+1,taken^(1<<i)^(1<<j)))
            # steps-=1
            return ans
        return solve(0,0)