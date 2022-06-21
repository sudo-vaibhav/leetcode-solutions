#User function Template for python3
from math import inf
from functools import lru_cache
class Solution:
    def matrixMultiplication(self, N, arr):
        
        @lru_cache(maxsize=None)
        def solve(start,end):
            if end-start>=2:
                ans = inf
                for mid in range(start+1,end):
                    ans = min(ans, solve(start,mid)+solve(mid,end)+arr[start]*arr[mid]*arr[end])
                return ans
            else: return 0
        
        return solve(0,N-1)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends