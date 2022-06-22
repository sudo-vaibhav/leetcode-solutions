#User function Template for python3
from functools import lru_cache
from math import inf
class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        @lru_cache(maxsize=None)
        def solve(floors,eggs):
            if floors<=1:return 1
            if eggs==1:return floors
            ans = inf
            for curDrop in range(1,floors+1):
                ans = min(ans,1+max(solve(curDrop-1,eggs-1),solve(floors-curDrop,eggs)))
            return ans
        return solve(k,n)
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends