class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        ans = []
        for w in words:
            ct = Counter(w)
            for k in ct:
                if c[k]<ct[k]:
                    break
            else:
                ans.append(w)
        return sum(map(len,ans))