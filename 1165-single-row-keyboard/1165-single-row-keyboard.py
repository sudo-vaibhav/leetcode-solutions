class Solution:
    def calculateTime(self, kb: str, word: str) -> int:
        prev = 0
        ans = 0
        for c in word:
            n = kb.index(c)
            ans += abs(n-prev)
            prev = n
        return ans