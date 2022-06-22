from functools import lru_cache
from math import inf
class Solution:
    def eggDrop(self,n, k):
        @lru_cache(maxsize=None)
        def solve(floors,eggs):
            if floors<=1: return floors
            if eggs==1:return floors
            ans = inf
            for curDrop in range(floors):
                ans = min(ans,1+max(solve(curDrop,eggs-1),solve(floors-curDrop-1,eggs)))
            return ans
        return solve(floors = k,eggs = n)


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