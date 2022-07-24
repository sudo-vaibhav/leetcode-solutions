class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        ans = 0
        while j<n:
            while j<n and nums[j]!=0:
                j+=1
            i = j
            while j<n and nums[j]==0:
                j+=1
            
            count = j-i
            ans += (count*(count+1))//2
        return ans