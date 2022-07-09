class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = paragraph.lower()
        for sym in "!?',;. ":
            para = ",".join(para.split(sym))
        
        # temp = paragraph.lower().split("")
        temp = filter(lambda x:bool(x),para.split(","))
        ctr = Counter(temp)
        words = list(ctr.keys())
        # print(ctr)
        banned = set(banned)
        words.sort(key=lambda x : ctr[x],reverse=True)
        
        for word in words:
            if word not in banned:
                return word
        return ""