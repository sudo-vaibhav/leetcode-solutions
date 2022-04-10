class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 7+(10**9)
        n = len(nums)
        heapify(nums)
        while k:
            k-=1
            cur = heappop(nums)
            cur+=1
            heappush(nums,cur)
        prod = 1
        for n in nums:
            prod*=n
            prod%=MOD
        return prod