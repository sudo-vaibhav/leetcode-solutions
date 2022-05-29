#User function Template for python3
from math import inf
from functools import lru_cache
class Solution:
    
    
	def minCoins(self, coins, N, V):
	    coins.sort(reverse=True)
		@lru_cache(maxsize=None)
		def solve(idx,target):
		    if target==0:
		        return 0
		    if target<0:
		        return inf
		    if idx==N:
		        if target==0:
		            return 0
		        else:return inf
		    else:
		        cur = coins[idx]
		        return min(1+solve(idx,target-cur),solve(idx+1,target))
		
		ans = solve(0,V) 
		return -1 if ans==inf else ans 
		# code here

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