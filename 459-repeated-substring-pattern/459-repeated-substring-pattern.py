class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        S = s+s
        return s in S[1:-1]
        
        
        