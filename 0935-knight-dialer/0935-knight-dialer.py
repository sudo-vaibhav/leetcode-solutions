class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9+7
        nextPos = {
            1:[8,6],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[7,0,1],
            7:[2,6],
            8:[1,3],
            9:[4,2],
            0:[4,6]
        }
        @cache
        def solve(currentPos,stepsLeft):
            if stepsLeft==0:return 1
            ans = 0
            for nextP in nextPos[currentPos]:
                ans+=solve(nextP,stepsLeft-1)
            return ans
            
        ans = 0
        for start in range(0,10):
            
            ans = (ans+solve(start,n-1))%MOD
        
        return ans