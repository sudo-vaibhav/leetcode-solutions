class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ct = list(Counter(s).values())
        return ct == [ct[0]]*len(ct)