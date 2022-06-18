Trie = lambda : defaultdict(Trie)
WEIGHT = "weight"
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for idx, word in enumerate(words):
            cur = self.trie
            cur[WEIGHT] = idx
            for i in range(len(word)):
#               put prefixes assuming suffix ends
                tmp = cur
                for c in word[i:]:
                    tmp = tmp[c,None]
                    tmp[WEIGHT]=idx
                
#               put suffixes assuming prefix ends
                tmp = cur
                for c in word[:-i][::-1]:
                    tmp = tmp[None,c]
                    tmp[WEIGHT]=idx
                
                nex = cur[word[i],word[~i]]
                nex[WEIGHT] = idx
                cur = nex
        
    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        suffix = suffix[::-1]
        for i in range(max(len(prefix),len(suffix))):
            pre,suf = prefix[i] if i<len(prefix) else None,suffix[i] if i<len(suffix) else None
            if (pre,suf) not in cur: return -1
            cur = cur[pre,suf]
        return cur[WEIGHT]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)