class Solution:
    def angleClock(self, h: int, m: int) -> float:
        temp = abs(m*5.5-30*h)
        return min(360-temp, temp)