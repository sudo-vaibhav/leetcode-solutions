class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        base,a = 26,ord("a")
        MOD = 2**63-1
        def getAlloc(s):
            ans,c,alloc = 0,0,[None]*26
            for i in s:
                ans,i = (ans*base)%MOD,ord(i)-a
                if alloc[i]==None:
                    alloc[i]=c
                    c+=1
                ans += alloc[i]
                if ans>=MOD:
                    ans -= MOD
            return ans
        main = getAlloc(pattern)
        return [w for w in words if getAlloc(w)==main]