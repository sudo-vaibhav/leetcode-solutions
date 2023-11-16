class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        
        for i in range(n):
            pos = (n-i-1)*"0"+"1"+"0"*i
            
            if pos not in nums:
                return pos
        
        return "0"*n