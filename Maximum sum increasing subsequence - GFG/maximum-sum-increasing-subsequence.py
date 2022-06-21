#User function Template for python3
from functools import lru_cache
class Solution:
	def maxSumIS(self, Arr, n):
        @lru_cache(maxsize=None)
        def solve(i):
            ans = Arr[i]
            for nex in range(i+1,n):
                if Arr[nex]>Arr[i]:
                    ans = max(ans,Arr[i]+solve(nex))
            return ans
                
        return max([solve(i) for i in range(n)])
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends