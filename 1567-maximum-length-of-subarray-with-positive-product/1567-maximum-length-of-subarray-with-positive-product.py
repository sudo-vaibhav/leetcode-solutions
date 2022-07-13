class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        
        pos,neg = 0,0
        ans = 0
        for num in nums:
            
            if num==0:
                pos,neg = 0,0
            elif num>0:
                
                pos+=1
                neg = neg+1 if neg>0 else 0
            
            else: # num<0
                temp  = pos
                pos = 0 if neg==0 else neg+1
                neg = temp+1
            
            ans = max(ans,pos)
        
        return ans