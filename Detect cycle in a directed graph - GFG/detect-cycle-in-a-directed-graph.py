#User function Template for python3
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        q,ans,indegree = deque(),[],{i:0 for i in range(V)}
        for i in range(V):
            for j in adj[i]: indegree[j]+=1
        for i in range(V):
            if indegree[i]==0: q.append(i)
        cnt=0
        while q:
            cur = q.popleft()
            ans.append(cur)
            for dest in adj[cur]:
                indegree[dest]-=1
                if indegree[dest]==0: q.append(dest)
            cnt+=1
        return cnt!=V

#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends