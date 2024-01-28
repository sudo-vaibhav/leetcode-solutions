from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])
        
        # compute 2D prefix sum
        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]
        
        count = 0
        # reduce 2D problem to 1D one
        # by fixing two columns c1 and c2 and 
        # computing 1D prefix sum for all matrices using [c1..c2] columns
        for c1 in range(1, c + 1):
            for c2 in range(c1, c + 1):
                h = defaultdict(int)
                h[0] = 1
                
                for row in range(1, r + 1):
                    # current 1D prefix sum 
                    curr_sum = ps[row][c2] - ps[row][c1 - 1]
                    
                    # add subarrays which sum up to (curr_sum - target)
                    count += h[curr_sum - target]
                    
                    # save current prefix sum
                    h[curr_sum] += 1
                    
        return count