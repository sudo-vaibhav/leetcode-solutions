class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans= 0
        while k>0 or any(map(lambda x:x!=0,nums)):
            cur = k&1
            count = 0
            for i in range(n):
                count += nums[i]&1
                nums[i]>>=1
            if cur==1 and count%2==0:
                ans +=1
            if cur==0 and count%2==1:
                ans +=1
            k>>=1
        return ans
                