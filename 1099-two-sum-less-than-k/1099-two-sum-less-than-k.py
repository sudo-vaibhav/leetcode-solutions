class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # ctr = Counter(nums)
        maxSum = -1
        nums.sort()
        l,r = 0,len(nums)-1
        
        while l<r:
            n1,n2 = nums[l],nums[r]
            tot = n1+n2
            if tot<k:
                maxSum = max(maxSum,tot)
                l+=1
            else:
                r-=1
        return maxSum
        