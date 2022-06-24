#User function Template for python3
from math import inf
class Solution:
    def bellman_ford(self, V, edges, S):
        dist = [10**8]*V
        dist[S] = 0
        for relaxIdx in range(1,V+1):
            for u,v,wt in edges:
                if dist[u]+wt<dist[v]:
                    if relaxIdx==V:
                        print("cycle detected")
                    dist[v] = dist[u]+wt
        return dist
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends