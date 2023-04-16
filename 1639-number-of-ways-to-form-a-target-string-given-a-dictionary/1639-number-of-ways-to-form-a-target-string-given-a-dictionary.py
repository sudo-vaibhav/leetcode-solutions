class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m,n = len(words),len(words[0])
        
        wordsByCol = defaultdict(lambda:defaultdict(int))
        for col in range(n):
            for row in range(m):
                wordsByCol[col][words[row][col]]+=1
        
        MOD = 10**9+7
        
        @cache
        def solve(charIdx, colIdx):
            if charIdx==len(target):
                return 1
            if colIdx==n: return 0
            cur = target[charIdx]
            ans = (solve(charIdx,colIdx+1)+wordsByCol[colIdx][cur]*solve(charIdx+1,colIdx+1))%MOD
            return ans
        
        return solve(0,0)