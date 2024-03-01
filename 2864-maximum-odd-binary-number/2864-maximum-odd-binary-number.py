class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ctr = Counter(s)
        if ctr["1"]==0:
            return 0
        
        return (ctr["1"]-1)*"1"+ctr["0"]*"0"+"1"