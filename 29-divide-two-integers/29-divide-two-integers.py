class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mul = 1 if (dividend/divisor)>0 else -1
        ans = mul*(abs(dividend)//abs(divisor))
        if ans>(-1+2**31):
            return -1+2**31
        elif ans<-1*(2**31):
            return -1*(2**31)
        return ans