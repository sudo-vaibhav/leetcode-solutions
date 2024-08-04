class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        seen = []
        MOD = 10**9+7
        for i in range(n):
            running = 0
            for j in range(i,n):
                running += nums[j]
                seen.append(running%MOD)
                
        seen.sort()
        # print(seen)
        return sum(seen[left-1:right])%MOD