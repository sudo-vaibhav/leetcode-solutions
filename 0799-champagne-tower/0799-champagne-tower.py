class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        fullness = defaultdict(lambda : defaultdict(int))
        fullness[0][0]+=poured
        
        for row in range(query_row+1):
            for glass in range(row+1):
                if fullness[row][glass]>1:
                    split = (fullness[row][glass]-1)/2
                    fullness[row+1][glass]+=split
                    fullness[row+1][glass+1]+=split
        return min(1,fullness[query_row][query_glass])