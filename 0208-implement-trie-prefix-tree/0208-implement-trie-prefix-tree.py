class Trie:

    def __init__(self):
        Trie = lambda : defaultdict(Trie)
        self.t = Trie()

    def insert(self, word: str) -> None:
        temp = self.t
        for c in word:
            nex = temp[c]
            nex["prefix"] = True
            temp = nex
            
        temp["word"] = True
        
    def search(self, word: str) -> bool:
        temp = self.t
        for c in word:
            nex = temp[c]
            temp = nex
        return "word" in temp

    def startsWith(self, prefix: str) -> bool:
        temp = self.t
        for c in prefix:
            nex = temp[c]
            temp = nex
        return "prefix" in temp

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)