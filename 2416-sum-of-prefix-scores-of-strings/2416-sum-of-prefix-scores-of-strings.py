class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        TR = lambda : defaultdict(TR)
        tr = TR()
        
        for word in words:
            temp = tr
            
            for c in word:
                temp = temp[c]
                if "score" in temp:
                    temp["score"] += 1
                else:
                    temp["score"] = 1
        ans = []
        for word in words:
            r = 0
            temp = tr
            for c in word:
                temp = temp[c]
                if "score" in temp:
                    r += temp["score"]
            ans.append(r)
        return ans