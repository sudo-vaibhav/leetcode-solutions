class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def solve(i,j):
            if(j-i<=1): return 0
            # if(j-i==1): return 1
            ans = float("inf")
            for k in cuts:
                if k>i and k<j:
                    tempans = j-i + solve(i,k)+solve(k,j)
                    ans = min(tempans,ans)
            if ans == float("inf"): return 0
            return ans
        return solve(0,n)