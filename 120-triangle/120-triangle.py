class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        M = len(triangle)
        @cache
        def solve(row,col):
            if row==M:
                return 0
            else:
                N = len(triangle[row])
                if 0<=col<N:
                    cur = triangle[row][col]
                    return cur + min(solve(row+1,col),solve(row+1,col+1))
                else:
                    return inf
            
        return solve(0,0)