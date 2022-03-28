class Solution:
    def numTrees(self, n: int) -> int:
        nodes = [i for i in range(1,n+1)]
        
        @cache
        def solve(nCount):
            if nCount<=1: return 1
            c=0
            for rootNo in range(1,nCount+1):
                c+= solve(rootNo-1)*solve(nCount-rootNo)
            return c
        
        return solve(n)