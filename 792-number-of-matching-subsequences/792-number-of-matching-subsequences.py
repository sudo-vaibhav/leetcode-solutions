class Solution:
    @cache
    def isSubsequence(self, s: str, t: str) -> bool:
        sIdx,tIdx,S,T = 0,0,len(s),len(t)
        while sIdx<S and tIdx<T:
            sIdx+=(s[sIdx]==t[tIdx])
            tIdx+=1
        return sIdx==S
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            count += self.isSubsequence(word,s)
        return count