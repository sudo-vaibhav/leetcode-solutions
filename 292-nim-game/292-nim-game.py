class Solution:
    def canWinNim(self, n: int) -> bool:
        
        # @cache
        # def playOptimal(cur):
        #     if cur>=n-2:
        #         return True
        #     for pickCount in range(1,3+1):
        #         if not playOptimal(cur+pickCount):
        #             return True
        #     return False
        if n%4==0:
            return False
                
        return True