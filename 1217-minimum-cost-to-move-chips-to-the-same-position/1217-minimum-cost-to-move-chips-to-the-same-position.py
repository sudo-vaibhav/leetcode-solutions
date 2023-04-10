class Solution:
    def minCostToMoveChips(self, pos: List[int]) -> int:
        
        odd=0
        n = len(pos)
        
        for i in pos:
            if i%2==1:
                odd+=1
        
        if odd>n-odd:
            return n-odd
        else:
            return odd
            