class Solution:
    def largestVariance(self, s: str) -> int:
        s = list(s)
        chars = list(set(s))
        res = 0
        for c1 in chars:
            for c2 in chars:
                variance,hasC2,firstC2 = 0,0,0
                
                for c in s:
                    variance += c==c1
                    if c==c2:
                        hasC2 = True
                        
                        if firstC2 and variance>=0:
                            firstC2 = False
                        elif variance-1<0:
                            variance = -1
                            firstC2 = True
                        else:
                            variance -= 1
                    
                    if hasC2 and variance>res:
                        res = variance
        return res
                
                        