class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        y = 0
        LEN = len(s)
        mat = ["" for _ in range(numRows)]
        # m,n = len(mat),len(mat[0])
        down = False
        ans = ""
        for i in range(len(s)):
            mat[y] += s[i]
            if y==numRows-1 or y==0:
                down=not down
            if down:
                y+=1
            else:
                y-=1
                    
        for row in mat:
            ans+= row
        return ans