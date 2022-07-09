class Solution:
    def checkString(self, s: str) -> bool:
        if "a" in s and "b" in s:
            A = len(s)-1-s[::-1].index("a")
            B = s.index("b")
            return A<B
        return True