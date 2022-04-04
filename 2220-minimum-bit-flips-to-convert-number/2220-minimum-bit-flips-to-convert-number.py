class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = str(bin(start^goal))
        return x[1:].count("1")