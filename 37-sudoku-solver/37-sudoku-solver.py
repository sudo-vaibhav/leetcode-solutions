class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)
        empty = "."
        
        def willConflict(row,col,num):
#             check in cur row
            NUM = str(num)
            for c in range(n):
                if board[row][c]==NUM:return True
            for r in range(n):
                if board[r][col]==NUM:return True
#           in current 3x3 box
            R = row//3
            C = col//3
            
            for r in range(R*3,3*R+3):
                for c in range(3*C,3*C+3):
                    if board[r][c]==NUM:
                        return True
            return False
            
        def solve(row,col):
            if col==n:return True
            nextRow = (row+1)%n
            nextCol = col+1 if row == n-1 else col
            
            if board[row][col]!=empty:
                return solve(nextRow,nextCol)
            else:
                for num in range(1,n+1):
                    if not willConflict(row,col,num):
                        board[row][col]=str(num)
                        temp = solve(nextRow,nextCol)
                        if temp:
                            return True
                        board[row][col]=empty

            return False
                
        
        solve(0,0)
        