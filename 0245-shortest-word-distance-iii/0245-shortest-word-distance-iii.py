class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ans = inf
        if word1==word2:
            lastOcc = -1
            for idx,word in enumerate(wordsDict):
                if word==word1:
                    if lastOcc!=-1:
                        ans = min(ans,idx-lastOcc)
                    lastOcc = idx
        else:
            o1,o2 = -1,-1
            for idx,word in enumerate(wordsDict):
                if word==word1:
                    o1 = idx
                elif word==word2:
                    o2 = idx
                
                if min(o1,o2)>-1:
                    ans = min(ans,abs(o2-o1))
                    
            
        return ans