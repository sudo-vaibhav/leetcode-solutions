class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = []
        x = 1
        
        while x<=10**9:
            nums.append(Counter(str(x)))
            x*=2
        
        # print(nums)
        temp = Counter(str(n))
        for n in nums:
            if n==temp:
                return True
        return False