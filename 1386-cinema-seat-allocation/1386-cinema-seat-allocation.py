class Solution:
    def maxNumberOfFamilies(self, n: int, seats: List[List[int]]) -> int:
        ans = n*3
        
        burnt = defaultdict(set)
        for row,col in seats:
            
            if 2<=col<=5:
                burnt[row].add(0)
            if 4<=col<=7:
                burnt[row].add(1)
            if 6<=col<=9:
                burnt[row].add(2)
                
        brows = list(burnt.keys())
        ub = n-len(brows)
        ans = 0
        for r in brows:
            ans += min(1,3-len(burnt[r]))
            
        return ub*2 + ans