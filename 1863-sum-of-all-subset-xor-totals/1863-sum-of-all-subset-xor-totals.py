class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1,len(nums)+1):
            
            for comb in combinations(nums,i):
                ans += reduce(lambda a,b : a^b,comb)
        return ans
        # return sum(map(lambda x:reduce(lambda a,b: a^b,0),))