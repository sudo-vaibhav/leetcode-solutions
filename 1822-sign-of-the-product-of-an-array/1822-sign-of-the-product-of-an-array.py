class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negCount = 0
        zero = False
        for num in nums:
            if num<0:
                negCount+=1
            if num==0:
                zero=True
                break
        
        if zero:
            return 0
        if negCount%2==1:
            return -1
        return 1