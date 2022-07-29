class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        base = 26
        MOD = 2**63-1
        def getAlloc(s):
            ans,c,alloc = 0,0,{}
            for i in s:
                ans = (ans*base)%MOD
                if i not in alloc:
                    alloc[i]=c
                    c+=1
                ans += alloc[i]
                if ans>=MOD:
                    ans -= MOD
            return ans
        main = getAlloc(pattern)
        return [w for w in words if getAlloc(w)==main]