TR = lambda : defaultdict(TR)
WORD = "word"
class Trie:
    def __init__(self):
        self.root = TR()
    def insert(self, word: str) -> None:
        tmp = self.root
        for c in word:
            tmp = tmp[c]
        tmp[WORD]=True
    def search(self, word: str) -> bool:
        tmp = self.root
        for c in word:
            if c not in tmp: return False
            tmp = tmp[c]
        return WORD in tmp
    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        for c in prefix:
            if c not in tmp: return False
            tmp = tmp[c]
        return len(tmp.keys())>0