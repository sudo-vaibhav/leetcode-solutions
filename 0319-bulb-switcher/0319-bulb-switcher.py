class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        # pos1 -> toggled once 
        
        # pos2 -> toggled 2 times
        # 1 - 1
        # 2 - 1 2
        # 3 - 1 3
        # 4 - 1 2 4
        # 5 - 1 5
        # 6 - 1 2 3
        # 7 - 1 7 
        # 8 - 1 2 4 8
        # 9 - 1 3 9
        # 10 - 1 2 5 10
        # 11 - 1 11
        # 12 - 1 2 3 4 6 12
        # 13 - 1 13
        
#         only composite mein count karo
        
        # 1,4,6,9,
        
        return int((n)**0.5)