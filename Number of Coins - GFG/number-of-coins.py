#User function Template for python3
from math import inf
from functools import lru_cache
class Solution:
    
    
	def minCoins(self, coins, N, V):
        @lru_cache(maxsize=None)
        def minCoinCount(target):
            if target==0: return 0
            # if target<0: return inf
            ans = inf
            for coin in coins:
                if coin<=target:
                    ans = min(ans,1+minCoinCount(target-coin))
            return ans
        res = minCoinCount(V)
        return -1 if res==inf else res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends