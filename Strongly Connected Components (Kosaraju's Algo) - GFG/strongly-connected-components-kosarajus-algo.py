#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        seen = set()
        topoSort = []
        def topo(node):
            if node in seen:return
            seen.add(node)
            for dest in adj[node]:
                topo(dest)
            topoSort.append(node)
        for i in range(V): topo(i)
        topoSort.reverse()
        ccCount = 0
        vis = set()
        revAdj = [[] for _ in range(V)]
        for i in range(V):
            for dest in adj[i]:
                revAdj[dest].append(i)
        def dfs(node):
            if node in vis: return
            vis.add(node)
            for dest in revAdj[node]:
                dfs(dest)
        for node in topoSort:
            if node not in vis:
                dfs(node)
                ccCount+=1
        return ccCount
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends