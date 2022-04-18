class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        wordLen = len(words[0])
        totalSubLen = wordLen*len(words)
        ws = set(words)
        words = Counter(words)
        
        def check(idx):
            end = idx+totalSubLen
            x = {}
            if end>n:
                return False
            else:
                for i in range(idx,end,wordLen):
                    temp = s[i:i+wordLen] 
                    if temp not in ws:
                        return False
                    else:
                        x[temp] = 1 if temp not in x else x[temp]+1
                return x==words
            
        ans = []
        for i in range(n):
            if check(i):    
                ans.append(i)
        return ans