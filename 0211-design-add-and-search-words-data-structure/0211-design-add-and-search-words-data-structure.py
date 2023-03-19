class WordDictionary:

    def __init__(self):
        Trie = lambda : defaultdict(Trie)
        self.t = Trie()

    def addWord(self, word: str) -> None:
        temp = self.t
        for c in word:
            temp = temp[c]
        temp["word"]=True

    def search(self, word: str) -> bool:
        n = len(word)
        def solve(i,root):
            if i==n: return "word" in root
            c = word[i]
            if c==".":
                for candidate in root:
                    if candidate!="word":
                        if solve(i+1,root[candidate]): return True
                return False
            else:
                if c not in root: return False
                return solve(i+1,root[c])
        return solve(0,self.t)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)