class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        def surroundCount(c):
            ans = 0
            for i in range(1,n-1):
                if colors[i]==c and colors[i-1]==c and colors[i+1]==c:
                    ans += 1
            return ans
        
        a= surroundCount("A")
        b= surroundCount("B")
        return a>b