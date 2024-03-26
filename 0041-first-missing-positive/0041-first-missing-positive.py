class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = sorted(set(filter(lambda x:x>0,nums)))
        # i=1 
        # try:
        #     while True:
        #         if nums[i-1]!=i:
        #             return i
        #         i+=1
        # except:
        #     return len(nums)+1
        n = len(nums)
        for i in range(n):
            if nums[i]<=0:
                nums[i]=inf
        for i in range(n):
            if nums[i]!=inf:
                val = abs(nums[i])
                if val<=n:
                    nums[val-1]=-abs(nums[val-1])
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1