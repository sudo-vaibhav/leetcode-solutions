class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s)==1: return ""
        n = len(s)
        # if s=="a"*n:
        #     return s[:-1]+"b"
        # else:
        for i in range(n//2):
            if s[i]!="a":
                return s[:i]+"a"+s[i+1:]
        return s[:-1]+"b"
        # lowest = None
        # for i in range(n): # O(n)
        #     cur = s[i]
        #     for rw in string.ascii_lowercase:# O(1)
        #         temp = s[:i]+rw+s[i+1:]
        #         if rw!=cur and temp!=temp[::-1] and (lowest==None or temp<lowest): # O(n)
        #             lowest = temp
        # return lowest