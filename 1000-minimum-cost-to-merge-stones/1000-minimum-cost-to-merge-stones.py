class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        
        N = len(stones)
        
#         N - v(k-1) = 1

        if (N-1)%(k-1)==0:
            @cache
            def solve(i,j,piles):
                ans = inf
                if i==j:
                    if piles==1:
                        return 0
                    else:
                        return inf
                else:
                    if piles==1:
                        temp = solve(i,j,k)
                        if temp!=inf:
                            ans = temp + sum(stones[i:j+1])
                    else:
                        for end in range(i,j):
                            l = solve(i,end,piles-1)
                            r = solve(end+1,j,1)
                            ans = min(ans,l+r)#+sum(stones[i:j+1]))
                return ans
                        
            return solve(0,N-1,1)
        else:
            return -1