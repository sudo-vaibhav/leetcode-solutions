class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        c = Counter(nums)[1]
        ans = len(nums)
        n = len(nums)
        @cache
        def onesTill(i):
            if i<0:
                return 0
            return int(nums[i]==1) + onesTill(i-1)
        # print(nums,[onesTill(i) for i in range(len(nums))])
        for i in range(len(nums)):
            if i>=c-1:
                ans = min(ans,c-(onesTill(i)-(onesTill(i-c) if i>=c else 0)))
            else:
                leftOnes = onesTill(i)
                leftExpected = i+1
                rightExpected = c-leftExpected
                rightOnes = onesTill(n-1)-onesTill(n-rightExpected-1)
                ans = min(ans,leftExpected-leftOnes+rightExpected-rightOnes)
        return ans