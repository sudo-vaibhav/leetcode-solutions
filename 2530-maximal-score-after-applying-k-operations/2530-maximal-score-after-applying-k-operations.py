class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hp = []
        
        for i in nums:
            heappush(hp,-i)
        ans = 0
        
        while k:
            num = -heappop(hp)
            ans += num
            heappush(hp,-ceil(num/3))
            k-=1
        return ans