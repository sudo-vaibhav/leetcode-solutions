class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        
        ans = min(nums)
        # while ans>=10:
        ans = sum(map(int,str(ans)))
        return 1 if ans%2==0 else 0