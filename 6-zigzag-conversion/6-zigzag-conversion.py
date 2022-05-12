class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        x,y = 0,0
        LEN = len(s)
        mat = [["" for _ in range(1000)] for _ in range(numRows)]
        m,n = len(mat),len(mat[0])
        down = True
        for i in range(len(s)):
            # print(x,y)
            mat[y][x] = s[i]
            if y==numRows-1:
                down=False
            elif y==0:
                down =True
            if down:
                y+=1
            else:
                y-=1
                x+=1
        ans = ""
        for row in mat:
            ans+= "".join(row)
        return ans