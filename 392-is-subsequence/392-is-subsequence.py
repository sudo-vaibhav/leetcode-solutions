class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Recursive Solution         
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
        sIdx,tIdx = 0,0
        while sIdx<len(s) and tIdx<len(t):
            sIdx+=(s[sIdx]==t[tIdx])
            tIdx+=1
        return sIdx==len(s) 
            