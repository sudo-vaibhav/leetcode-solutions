class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
#         color = {}
#         def dfs(node,col):
#             color[node]=col
#             for dest in graph[node]:
#                 if dest in color:
#                     if color[dest]==col: return False
#                 else:
#                     if not dfs(dest,1-col):return False
#             return True
        
#         for node in range(len(graph)):
#             if node not in color:
#                 if not dfs(node,0): return False
#         return True
        color = {}
        q = deque()
        for node in range(len(graph)):
            if node not in color:
                q.append(node)
                color[node] = 0
                while q:
                    curNode = q.popleft()
                    for dest in graph[curNode]:
                        if dest in color:
                            if color[dest]==color[curNode]:return False
                        else:
                            color[dest]=1-color[curNode]
                            q.append(dest)
        return True