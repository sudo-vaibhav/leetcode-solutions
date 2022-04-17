class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        @cache
        def factors(num):
            ans = [0,0]
            while num%2==0:
                ans[0]+=1
                num/=2
            while num%5==0:
                ans[1]+=1
                num/=5
            return tuple(ans)
        
        top = [[[0,0] for i in range(n)] for j in range(m)]
        left = [[[0,0] for i in range(n)] for j in range(m)]
        bottom = [[[0,0] for i in range(n)] for j in range(m)]
        right = [[[0,0] for i in range(n)] for j in range(m)]
        
        def sum_factors(p1,p2):
            return [p1[0]+p2[0],p1[1]+p2[1]]
        
        def diff_and_min(p1,p2):
            return min([p1[0]-p2[0],p1[1]-p2[1]])
        
        
        for row in range(m):
            for col in range(n):
                top[row][col] = sum_factors(factors(grid[row][col]),top[row-1][col] if row>0 else [0,0])
                left[row][col] = sum_factors(factors(grid[row][col]),left[row][col-1] if col>0 else [0,0])
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                bottom[row][col] = sum_factors(factors(grid[row][col]),bottom[row+1][col] if row<m-1 else (0,0))
                right[row][col] = sum_factors(factors(grid[row][col]),right[row][col+1] if col<n-1 else (0,0))
        
        ans = 0
        for row in range(m):
            for col in range(n):
                curFac = factors(grid[row][col])
                ans = max(
                        ans,
                        diff_and_min(sum_factors(top[row][col],right[row][col]),curFac),
                        diff_and_min(sum_factors(top[row][col],left[row][col]),curFac),
                        diff_and_min(sum_factors(bottom[row][col],right[row][col]),curFac),
                        diff_and_min(sum_factors(bottom[row][col],left[row][col]),curFac)
                     )
                
        return ans
                
                