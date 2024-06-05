class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = list(map(Counter,words))
        ans = l[0]
        for i in l[1:]:
            for c in range(26):
                ans[chr(ord("a")+c)] = min(ans[chr(ord("a")+c)],i[chr(ord("a")+c)])
            # ans = ans.intersection(i)
        res = []
        for c in range(26):
            res.extend([chr(ord("a")+c)]*ans[chr(ord("a")+c)])
        return res