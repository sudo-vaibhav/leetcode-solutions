class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1,words2 = Counter(words1),Counter(words2)
        
        w1,w2 = set(words1.keys()),set(words2.keys())
        
        fw = w1.intersection(w2)
        
        ans = 0
        for w in fw:
            if words1[w]==1 and words2[w]==1:
                ans+=1
        return ans