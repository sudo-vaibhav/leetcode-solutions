class Solution:
    def makesquare(self,nums: List[int]) -> bool:
        
        tot = sum(nums)
        N = len(nums)
        if tot%4!=0 or N<4: return False
        sideLen = tot//4
        
        @cache
        def solve(used,completedSides):
            
            totalUsed = 0
            
            for i in range(N):
                if not (used & (1<<i)):
                    totalUsed += nums[i]
            
            if totalUsed>0 and totalUsed%sideLen==0:
                completedSides+=1
            
            if completedSides==3:
                return True
            
            remainingCap = (totalUsed//sideLen+1)*sideLen - totalUsed
            
            for i in range(N):
                if (used & 1<<i) and nums[i]<=remainingCap:
                    if solve(used ^ 1<<i,completedSides):
                        return True
            
            return False
        
        
        return solve((1<<N)-1,0)