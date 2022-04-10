# heapify(nums)
# while k:
#     k-=1
#     cur = heappop(nums)
#     cur+=1
#     heappush(nums,cur)
# m = -inf
# prod = 1
# for n in nums:
#     prod*=n
#     if prod>=MOD:
#         prod-=MOD
#     m = max(prod,m)
# return m
        
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 7+(10**9)
        n = len(nums)
        # @cache
        # def s(idx,k):
        #     if idx>=n: return 1
        #     if k<=0:
        #         p=1
        #         for g in nums[idx:]:
        #             p*=g
        #         return p
        #     m = 0
        #     for i in range(0,k+1):
        #         tempans = (nums[idx]+i)*s(idx+1,k-i)
        #         m = max(m,tempans)
        #     return m
        # return s(0,k)%MOD
        heapify(nums)
        while k:
            k-=1
            cur = heappop(nums)
            cur+=1
            heappush(nums,cur)
        # m = -inf
        prod = 1
        for n in nums:
            prod*=n
            prod%=MOD
            
            # m = max(prod,m)%MOD
        return prod