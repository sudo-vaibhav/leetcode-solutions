class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s)==1: return ""
        n = len(s)
        lowest = None
        for i in range(n): # O(n)
            cur = s[i]
            for rw in string.ascii_lowercase:# O(1)
                temp = s[:i]+rw+s[i+1:]
                if rw!=cur and temp!=temp[::-1] and (lowest==None or temp<lowest):
                    lowest = temp
        return lowest