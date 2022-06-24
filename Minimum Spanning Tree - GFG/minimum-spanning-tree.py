#User function Template for python3

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        class UF:
            def __init__(self,V):
                self.parent = [i for i in range(V)]
                self.rank = [0 for _ in range(V)]
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:return
                ru,rv = self.rank[pu],self.rank[pv]
                if ru<rv:
                    pu,pv = pv,pu
                    ru,rv = rv,ru
                self.parent[pv] = pu
                if ru==rv:
                    self.rank[pu]+=1
            def find(self,u):
                if self.parent[u]==u:return u
                self.parent[u] = self.find(self.parent[u])
                return self.parent[u]
        uf = UF(V)
        edges = []
        for i in range(V):
            for dest,wt in adj[i]:
                edges.append((i,dest,wt))
        edges.sort(key=lambda x :x[2])
        ans = 0
        for u,v,wt in edges:
            if uf.find(u)==uf.find(v): continue
            ans += wt
            uf.union(u,v)
        return ans
                    
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
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends