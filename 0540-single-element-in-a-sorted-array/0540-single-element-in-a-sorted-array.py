class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        if n==1: return nums[0]
        try:
            while l<=r:

                m = (l+r)//2

                if m%2==0:
                    if nums[m+1]!=nums[m]:
                        r=m-1
                    else:
                        l=m+1
                else:
                    if nums[m+1]!=nums[m]:
                        l=m+1
                    else:
                        r=m-1
        except:
            return nums[-1]
        # print(l)
        return nums[l]
        