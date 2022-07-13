class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        
        def solve(L,R):
            secondLast,last = 0,0
            cur = 0
            for i in range(L,R+1):
                cur = max(nums[i]+secondLast,last)
                secondLast = last
                last = cur
            return cur
        
        n = len(nums)
        return max(solve(1,n-1),solve(0,n-2))