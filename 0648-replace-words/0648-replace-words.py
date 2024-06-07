class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        TR = lambda : defaultdict(TR)
        tr = TR()
        
        for w in dictionary:
            temp = tr
            for c in w:
                temp = temp[c]
            temp["word"]=w
        # print(tr.keys())  
        ans = []
        
        for w in sentence.split():
            # print(w)
            temp = tr
            for c in w:
                temp = temp[c]
                if temp["word"]:
                    ans.append(temp["word"])
                    break
            else:
                # print(w)
                ans.append(w)
        return " ".join(ans)
                