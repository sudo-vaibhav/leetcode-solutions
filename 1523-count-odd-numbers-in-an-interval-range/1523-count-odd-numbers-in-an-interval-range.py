class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def isOdd(n): return n%2==1
        
        if high==low: return int(isOdd(high))
        if(isOdd(high) and isOdd(low)): return 1+((high-low)//2)
        if(not isOdd(high) and not isOdd(low)): return (high-low)//2
        return ceil((high-low)/2)