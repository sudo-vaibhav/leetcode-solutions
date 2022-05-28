class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur,highest = 0,0
        for num in nums:
            if num==1:
                cur+=1
            else:
                cur=0
            highest = max(cur,highest)
        
        return highest