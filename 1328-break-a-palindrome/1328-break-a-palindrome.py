class Solution:
    def breakPalindrome(self, s: str) -> str:
        
        if len(s)==1: return ""
        n = len(s)
        lowest = None
        for i in range(n):
            cur = s[i]
            for rw in string.ascii_lowercase:
                if rw!=cur:
                    temp = s[:i]+rw+s[i+1:]
                    if temp!=temp[::-1]:
                        if lowest==None or temp<lowest:
                            lowest = temp
        return lowest