class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        def solve(lg,md,LG,MD):
            if md>lg:
                return solve(md,lg,MD,LG)
            if md==0:
                return LG*min(2,lg)
            lg_used = min(2,lg)
            md_used = 1 if lg-lg_used>=md else 0
            return LG*lg_used+MD*md_used+solve(lg-lg_used,md-md_used,LG,MD)
        
        return solve(a,b,"a","b")