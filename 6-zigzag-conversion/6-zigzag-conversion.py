class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        y,LEN,down,ans = 0,len(s),False,""
        mat = [""]*numRows
        for i in range(len(s)):
            mat[y] += s[i]
            if y==numRows-1 or y==0:
                down=not down
            y += 1 if down else -1
        for row in mat:
            ans+= row
        return ans