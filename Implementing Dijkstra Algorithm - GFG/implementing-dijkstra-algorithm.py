from heapq import heappush,heappop
from math import inf
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        heap = []
        dists = [inf for _ in range(V)]
        dists[S] = 0
        heappush(heap,(0,S))
        while heap:
            curDist,curNode = heappop(heap)
            if curDist>dists[curNode]:
                continue
            for dest,wt in adj[curNode]:
                if curDist+wt<dists[dest]:
                    dists[dest] = curDist+wt
                    heappush(heap,(dists[dest],dest))
        return dists
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
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends