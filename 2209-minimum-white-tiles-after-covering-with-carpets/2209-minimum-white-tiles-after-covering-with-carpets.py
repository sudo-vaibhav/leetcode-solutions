class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        N = len(floor)
        @cache
        def solve(n,c):
            if n<=0:return 0
            # if c<=0: return 1000
            cover = solve(n-carpetLen,c-1) if c else inf
            notcover = int(floor[n-1]) + solve(n-1,c)
            return min(cover,notcover)
            
        return solve(N,numCarpets)