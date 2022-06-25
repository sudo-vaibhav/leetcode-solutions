class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        ct=0
        for i in range(1,n):
            # print(nums)           
            if nums[i]<nums[i-1]:
                if ct==1:return False
                if i>=2:
                    if nums[i]>=nums[i-2]:
                        nums[i-1] = nums[i]
                    else:
                        nums[i]=nums[i-1]
                else:
                    nums[i-1] = nums[i]
                ct+=1
        # print(nums)
        return ct<=1