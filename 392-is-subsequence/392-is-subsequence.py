class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # def solve(sIdx, tIdx, s, t):
        #     if(sIdx==len(s)): return True
        #     if(tIdx==len(t)): return False
        #     sVal = s[sIdx]
        #     tVal = t[tIdx]
        #     if(tVal==sVal):
        #         return solve(sIdx+1,tIdx+1,s,t)
        #     else:
        #         return solve(sIdx,tIdx+1,s,t)
        # return solve(0,0,s,t)
        sIdx = 0
        tIdx = 0
        
        while True:
            if(sIdx==len(s)): return True
            if(tIdx==len(t)): return False
            sVal = s[sIdx]
            tVal = t[tIdx]
            if(tVal==sVal):
                sIdx+=1
                tIdx+=1
            else:
                tIdx+=1