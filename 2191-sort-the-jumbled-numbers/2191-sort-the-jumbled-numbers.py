class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        m = {str(k):str(mapping[k]) for k in range(10)}
        
        @cache
        def getVal(n):
            n = "".join([m[f] for f in str(n)])
            return int(n)
        nums = [(getVal(n),n) for n in nums]
        nums.sort(key=lambda x:x[0])
        return [n[1] for n in nums]