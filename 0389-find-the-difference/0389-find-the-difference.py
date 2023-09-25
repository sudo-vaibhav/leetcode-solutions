class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [x[0] for x in Counter(s+t).items() if x[1]%2][0]