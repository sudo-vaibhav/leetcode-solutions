class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        sq = []
        while i*i<=10**4:
            sq.append(i*i)
            i+=1
        
        left = n
        ans = []
        # print(sq)
        while left>0:
            for num in range(len(sq)-1,-1,-1):
                if sq[num]<=left:
                    left-=sq[num]
                    ans.append(sq[num])
                    break
        @cache
        def solve(n):
            if n==0:return 0
            ans = inf
            for num in sq:
                if num<=n:
                    ans = min(ans,1+solve(n-num))
            return ans
        return solve(n)