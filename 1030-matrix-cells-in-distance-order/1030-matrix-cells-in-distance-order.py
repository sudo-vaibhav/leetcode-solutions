class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        ans = []
        for i in range(rows):
            for j in range(cols):
                ans.append((abs(j-cCenter)+abs(i-rCenter),(i,j)))
        ans.sort()
        return map(lambda x:x[1],ans)