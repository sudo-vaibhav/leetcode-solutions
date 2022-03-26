class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ct = Counter(nums)
        for i in ct.values():
            if i%2==1:
                return False
        return True