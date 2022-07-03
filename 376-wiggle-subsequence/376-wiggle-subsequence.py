class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pos,neg = True, False
        n = len(nums)
        
        @cache
        def solve(idx,prevVal,desiredPattern):
            if idx==n:
                return 0
#           avoid elem case
            ans = solve(idx+1,prevVal,desiredPattern)
            
#           if can take cur, take cur
            diff = nums[idx]-prevVal 
            if (diff >0 and desiredPattern==pos) or (diff<0 and desiredPattern==neg):
                ans = max(ans,1+solve(idx+1,nums[idx],not desiredPattern))
    
            return ans
            
        
        return max(solve(0,-inf,pos),solve(0,inf,neg))