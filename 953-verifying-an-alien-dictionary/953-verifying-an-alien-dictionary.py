class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        # ans = False
        for i in range(0,n-1):
            word1,word2 = words[i],words[i+1]
            minLength = min(len(word1),len(word2))
            for idx in range(minLength):
                c1,c2 = word1[idx],word2[idx] 
                if c1!=c2:
                    if order.index(c1)>order.index(c2):
                        return False
                    else:
                        break
            else:
                if len(word1)>len(word2):
                    return False
                    
        return True