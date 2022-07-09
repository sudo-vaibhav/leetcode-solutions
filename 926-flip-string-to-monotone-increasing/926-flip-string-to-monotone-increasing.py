class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @cache
        def onesTill(idx):
            if idx<0: return 0
            return int(s[idx]=="1")+onesTill(idx-1)
        
        @cache
        def makeMono(idx):
            if idx<0:return 0
            cur = s[idx]
            
            if cur=="0":
                
                return min(makeMono(idx-1)+1,onesTill(idx))
            else:
                return makeMono(idx-1)
                
        
        return makeMono(len(s)-1)