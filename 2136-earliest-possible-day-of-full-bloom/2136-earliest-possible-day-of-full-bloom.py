from sortedcontainers import SortedSet
class Solution:
    def earliestFullBloom(self, pt: List[int], gt: List[int]) -> int:
        
        plants = sorted(zip(pt,gt),key=lambda x:-x[1])            
        day = 0
        fin = 0
        for p,g in plants:
            print(day,p,g)
            fin = max(fin,day+p+g)
            day+=p
        # print(day)
        return fin
