class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        begin,end = s.split(":")
        begCol,endCol = ord(begin[0]),ord(end[0])
        begRow,endRow = int(begin[1]),int(end[1])
        ans = []
        for col in range(begCol,endCol+1):
            COL = chr(col)
            for row in range(begRow,endRow+1):
                ans.append(COL+str(row))
        return ans