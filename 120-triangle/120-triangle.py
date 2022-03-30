class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def solve(ridx,cidx):
            if cidx>ridx+1: return inf
            if ridx==n: return 0
            ma = triangle[ridx][cidx]+min(solve(ridx+1,cidx),solve(ridx+1,cidx+1))
            return ma
        return solve(0,0)