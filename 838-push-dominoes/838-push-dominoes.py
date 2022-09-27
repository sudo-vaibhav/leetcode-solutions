class Solution:
    def pushDominoes(self, doms: str) -> str:
        
        prev = ""
        cur = doms
        while prev!=cur:
            new = cur.replace("R.L","xxx").replace("R.","RR").replace(".L","LL")
            prev = cur
            cur = new
        return cur.replace("xxx","R.L")