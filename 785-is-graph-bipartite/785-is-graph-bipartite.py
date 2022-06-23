class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(node,col):
            color[node]=col
            for dest in graph[node]:
                if dest in color and color[dest]==col:
                    return False
            for dest in graph[node]:
                if dest not in color:
                    if not dfs(dest,1-col):return False
            return True
        
        for i in range(len(graph)):
            if i not in color:
                if not dfs(i,0):
                    return False
        return True