class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while ans>=10:
            ans = sum(map(int,str(ans)))
        return ans