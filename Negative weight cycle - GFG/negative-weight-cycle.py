#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, V, edges):
		dist = [10**8]*V
        dist[0] = 0
        for relaxIdx in range(1,V+1):
            for u,v,wt in edges:
                if dist[u]+wt<dist[v]:
                    if relaxIdx==V:
                        return 1
                    dist[v] = dist[u]+wt
        return 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends