class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        
        if c[0]>1:
            return [0]*n
        p = 1
        q = 1
        for i in nums:
            p*=i
            if i!=0:
                q*=i
        ans = [p//i if i!=0 else q for i in nums ]
        return ans