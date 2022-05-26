class Solution:
    def hammingWeight(self, x: int) -> int:
        cnt =0
        while x>0:
            x&=x-1
            cnt+=1
        return cnt