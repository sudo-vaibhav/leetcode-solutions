class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        pres = defaultdict(set)
        
        for i in range(0,n,2):
            col,plac = [rings[i],int(rings[i+1])]
            pres[plac].add(col)
        
        return len([i for i in pres.values() if len(i)==3])