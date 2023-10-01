class Trie:

    def __init__(self):
        TR = lambda :defaultdict(TR)
        self.t = TR()

    def insert(self, word: str) -> None:
        temp = self.t
        for c in word:
            temp = temp[c]
            if "startsWith" not in temp:
                temp["startsWith"]=0
            temp["startsWith"]+=1
            
        if "count" not in temp:
            temp["count"]=0
            
        temp["count"]+=1
            

    def countWordsEqualTo(self, word: str) -> int:
        temp = self.t
        for c in word:
            temp = temp[c]
        if "count" in temp:
            return temp["count"]
        return 0
    def countWordsStartingWith(self, prefix: str) -> int:
        temp = self.t
        for c in prefix:
            temp = temp[c]
        if "startsWith" in temp:
            return temp["startsWith"]
        return 0

    def erase(self, word: str) -> None:
        temp = self.t
        for c in word:
            temp = temp[c]
            temp["startsWith"]-=1
        if "count" in temp and temp["count"]>0:
            temp["count"]-=1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)