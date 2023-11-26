class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n = map(len,[matrix,matrix[0]])
        
#         returns the area and row length of the biggest possible uno matrix possible, "starting" at i,j
#         def solve(i,j):
#             if i==m or j==n: return 0
#             D,R = solve(i+1,j),solve(i,j+1)
            
            
#         return solve(0,0)[0]

        # l,r = 1,m
        @cache
        def continuousOnesFrom(row,col):
            if row==m:return 0
            if matrix[row][col]==0: return 0
            return 1+continuousOnesFrom(row+1,col)
        
        ans = 0
        for startRow in range(m):
            numOnes = []
            for col in range(n):
                ones = continuousOnesFrom(startRow,col)
                # numOnes = min(ones,numOnes)
                numOnes.append(ones)
            numOnes.sort(reverse=True)
            
            for idx,num in enumerate(numOnes):
                ans = max(ans,num*(idx+1))
        return ans
        