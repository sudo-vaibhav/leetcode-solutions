class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        next_diffs = [
            (-1,-2),
            (-2,-1),
            (-2,1),
            (-1,2),
            (1,2),
            (2,1),
            (2,-1),
            (1,-2)
        ]
        
        in_bounds = lambda coord: all(map(lambda pos : 0<=pos<n,coord))
        
        @cache
        def solve(i,j,moves):
            if not in_bounds((i,j)): return 0
            if moves==0: return 1
            ans = 0
            for di,dj in next_diffs:
                I,J = i+di,j+dj
                if in_bounds((I,J)):
                    ans += solve(I,J,moves-1)  
            return ans
        
        return solve(row,column,k)/8**k