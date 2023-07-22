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
        
        is_in_bounds = lambda coord: all(map(lambda pos : 0<=pos<n,coord))
        
        @cache
        def count_possibilities(i,j,moves):
            if not is_in_bounds((i,j)): return 0
            if moves==0: return 1
            ans = 0
            for di,dj in next_diffs:
                I,J = i+di,j+dj
                if is_in_bounds((I,J)):
                    ans += count_possibilities(I,J,moves-1)  
            return ans
        total_possibilities = len(next_diffs)**k
        return count_possibilities(row,column,k)/total_possibilities