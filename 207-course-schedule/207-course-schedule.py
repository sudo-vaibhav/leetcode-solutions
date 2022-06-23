class Solution:
    def canFinish(self, V: int, pr: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for a,b in pr:
            adj[b].add(a)
        
        vis = {}
        def dfs(node):
            if node in vis:
                return vis[node] # true if cycle is there
            vis[node]=True
            for dest in adj[node]:
                if dfs(dest):
                    return True
            vis[node]=False
            return False
        for i in range(V):
            if dfs(i):
                return False
        return True
        
#         q,ans,indegree = deque(),[],{i:0 for i in range(V)}
#         for i in range(V):
#             for j in adj[i]: indegree[j]+=1
#         for i in range(V):
#             if indegree[i]==0: q.append(i)
#         cnt=0
#         while q:
#             cur = q.popleft()
#             ans.append(cur)
#             for dest in adj[cur]:
#                 indegree[dest]-=1
#                 if indegree[dest]==0: q.append(dest)
#             cnt+=1
#         return cnt!=V:
        
        