class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1,rowIndex+1):
            # print(row)
            row.append(1)
            for j in range(len(row)-2,0,-1):
                row[j]+=row[j-1]
        return row