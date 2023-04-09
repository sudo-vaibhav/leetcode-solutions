class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ct = Counter(s)
        
        return len(list(filter(lambda x:x%2==1,ct.values())))<=1