class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l,r=0,0
        ct = 0
        for i in range(len(s)):
            cur = s[i]
            if cur=="L":
                l+=1
            else:
                r+=1
            
            if l==r:
                ct+=1
                l,r=0,0
        return ct