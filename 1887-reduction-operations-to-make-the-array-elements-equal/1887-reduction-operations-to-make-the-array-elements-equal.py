class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = list(sorted(Counter(nums).items(),reverse=True))
        # print(c)
        ops = 0
        elemsSoFar = c[0][1]
        for i in range(1,len(c)):
            ops += elemsSoFar
            elemsSoFar += c[i][1]
            
        return ops