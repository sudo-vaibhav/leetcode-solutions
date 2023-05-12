class Solution:
    @cache
    def divisorGame(self, n: int) -> bool:
        if n==1: return False
        return not self.divisorGame(n-1)
        