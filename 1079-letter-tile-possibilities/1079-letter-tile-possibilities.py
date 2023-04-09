class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        ans = set()
        chars = list(tiles)
        
        def solve(prev=""):
            if not chars: ans.add(str(prev))
            view = list(chars)
            
            for c in view:
                chars.remove(c)
                solve(prev+c)
                solve(prev)
                chars.append(c)
                
        solve()
        
        return len(ans)-1