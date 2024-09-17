class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1,c2 = map(Counter,[s1.split(),s2.split()])
        ws = set([*s1.split(),*s2.split()])
        ans = []
        for w in ws:
            if (c1[w]+c2[w]==1):
                ans.append(w)
        return ans