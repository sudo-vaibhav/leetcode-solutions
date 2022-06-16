class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        def solve(lg,md,sm,LG,MD,SM):
            if md>lg:
                return solve(md,lg,sm,MD,LG,SM)
            if sm>md:
                return solve(lg,sm,md,LG,SM,MD)
            if md==0:
                return LG*min(2,lg)
            lg_used = min(2,lg)
            md_used = 1 if lg-lg_used>=md else 0
            
            return (LG*lg_used)+(MD*md_used)+solve(lg-lg_used,md-md_used,sm,LG,MD,SM)
        
        
        
        return solve(a,b,c,"a","b","c")