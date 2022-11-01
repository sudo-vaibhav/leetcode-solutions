class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        ans = [-1]*n
        
        for ball in range(n):
            col = ball
            # print("ball",ball)
            for row in range(m):
                board = grid[row][col]
                
                if board==1: # TO RIGHT
                    if col+1<n and grid[row][col+1]==-1: break
                    col+=1
                else:
                    if col-1>=0 and grid[row][col-1]==1: break
                    col-=1
                # print(ball,row+1,col)
                if col<0 or col>=n:
                    break
            else:
                ans[ball]=col
        return ans