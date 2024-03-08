class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        f = max(c.values())
        ans = 0
        for k in c.keys():
            if c[k]==f:
                ans +=f
        
        return ans