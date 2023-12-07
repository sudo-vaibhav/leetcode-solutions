class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = -inf
        for n in "13579":
            try:
                l = max(l,num.rindex(n))
            except:
                pass
        if l==-inf:
            return ""
        
        return num[:l+1]
        # else: