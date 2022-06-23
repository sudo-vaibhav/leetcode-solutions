from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        q,ans,indegree = deque(),[],{i:0 for i in range(V)}
        for i in range(V):
            for j in adj[i]: indegree[j]+=1
        for i in range(V):
            if indegree[i]==0: q.append(i)
        while q:
            lenQ = len(q)
            for _ in range(lenQ):
                cur = q.popleft()
                ans.append(cur)
                for dest in adj[cur]:
                    indegree[dest]-=1
                    if indegree[dest]==0:
                        q.append(dest)
        return ans
#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends