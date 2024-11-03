class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            temp = s[i:]+s[:i]
            if temp==goal:
                return True
        return False