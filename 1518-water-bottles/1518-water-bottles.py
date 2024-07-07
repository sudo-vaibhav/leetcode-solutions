class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        emptyBottles = 0
        while numBottles>0 or emptyBottles>=numExchange:
            if numBottles>0:
                ans += numBottles
                emptyBottles += numBottles
                numBottles=0
            elif emptyBottles>=numExchange:
                numBottles += emptyBottles//numExchange
                emptyBottles %= numExchange
            
        return ans