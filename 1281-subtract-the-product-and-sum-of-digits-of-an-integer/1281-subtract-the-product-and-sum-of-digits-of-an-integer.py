class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int,list(str(n))))
        s = sum(digits)
        p = 1
        for dig in digits:
            p*=dig
        
        
        return p-s
                      