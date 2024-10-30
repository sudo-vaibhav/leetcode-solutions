class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        
#         @lru_cache(maxsize=10000)
#         def increasingWithMaxCap(i,maxCap):
#             if i==0:
#                 return int(nums[i]>=maxCap)
#             else:
#                 ans = 1+increasingWithMaxCap(i-1,maxCap)
#                 if nums[i]<maxCap:
#                     ans = min(ans,increasingWithMaxCap(i-1,nums[i]))
#                 return ans
#         @lru_cache(maxsize=10000)
#         def decreasingWithMaxCap(i,maxCap):
#             if i==n-1:
#                 return int(nums[i]>=maxCap)
#             else:
#                 ans = 1+decreasingWithMaxCap(i+1,maxCap)
#                 if nums[i]<maxCap:
#                     ans = min(ans,decreasingWithMaxCap(i+1,nums[i]))
#                 return ans
        lis = [1]*n
        lds = [1]*n
        
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    lis[i] = max(lis[i],1+lis[j])
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[i]>nums[j]:
                    lds[i] = max(lds[i],1+lds[j])
        # lRemovals = increasingWithMaxCap(pivot-1,nums[pivot])
        # rRemovals = decreasingWithMaxCap(pivot+1,nums[pivot])
        # # print(pivot,lRemovals,rRemovals,nums[pivot])
        # if lRemovals >= pivot:
        #     continue
        # if rRemovals >= n-1-pivot:
        #     continue
        
        for pivot in range(1,n-1):
            if lis[pivot]>1 and lds[pivot]>1:
                ans = min(n-(lis[pivot]+lds[pivot]-1),ans)
        return ans
        