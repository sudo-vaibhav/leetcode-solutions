#User function Template for python3
from math import inf
from functools import lru_cache
class Solution:
    
    
	def minCoins(self, coins, N, V):
    	    
        # table[i] will be storing the minimum 
        # number of coins required for i value. 
        # So table[V] will have result
        table = [0 for i in range(V + 1)]
    
        # Base case (If given value V is 0)
        table[0] = 0
    
        # Initialize all table values as Infinite
        for i in range(1, V + 1):
            table[i] = inf
            
        # Compute minimum coins required 
        # for all values from 1 to V
        for i in range(1, V + 1):
            
            # Go through all coins smaller than i
            for j in range(m):
                if (coins[j] <= i):
                    sub_res = table[i - coins[j]]
                    if (sub_res != inf and 
                        sub_res + 1 < table[i]):
                        table[i] = sub_res + 1
        
        if table[V] == inf:
            return -1
      
        return table[V]

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