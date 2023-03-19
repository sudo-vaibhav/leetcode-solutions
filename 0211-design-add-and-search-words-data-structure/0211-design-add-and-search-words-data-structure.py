class WordDictionary:

    def __init__(self):
        Trie = lambda : defaultdict(Trie)
        self.t = Trie()

    def addWord(self, word: str) -> None:
        temp = self.t
        for c in word: temp = temp[c]
        temp["word"]=True

    def search(self, word: str) -> bool:
        def solve(i,root):
            if i==len(word): return "word" in root
            c = word[i]
            if c==".":
                for key in root:
                    if key!="word" and solve(i+1,root[key]): return True
            return c in root and solve(i+1,root[c])
        return solve(0,self.t)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)