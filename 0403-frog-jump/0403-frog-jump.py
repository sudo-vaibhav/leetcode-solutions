class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        mapping = {}
        for idx, num in enumerate(stones):
            mapping[num]=idx
        @cache
        def solve(i,prevJump):
            if i==n-1: return True
            if i==0:
                if stones[i+1]!=stones[i]+1:return False
                return solve(i+1,1)
            else:
                for jumpSize in [prevJump-1,prevJump,prevJump+1]:
                    newArea = stones[i]+jumpSize
                    if newArea != stones[i] and newArea in mapping:
                        if solve(mapping[newArea],jumpSize):
                            return True
                return False
                
        return solve(0,1)