class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        
        xXorY = 0
        
        for i in range(1,n+1):
            xXorY^=i
        for i in nums:
            xXorY^=i
        
        b1 = 0
        b2 = 0
        
        for i in range(0,64):
            if (1<<i)&xXorY>0:
                break
        
        for j in range(1,n+1):
            if (1<<i)&j>0:
                b1^=j
            else:
                b2^=j
        
        for j in nums:
            if (1<<i)&j>0:
                b1^=j
            else:
                b2^=j
                
        return [b1,b2] if (b1 in nums) else [b2,b1]