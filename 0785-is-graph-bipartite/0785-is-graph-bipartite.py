class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        colors = defaultdict(lambda : -1)
        
        def solve(node):
            col = colors[node]
            for v in graph[node]:
                if colors[v]==col:
                    return False
                elif colors[v]==-1:
                    colors[v] = 1-col
                    if solve(v)==False:
                        return False
            return True
        
        for i in range(n):
            if colors[i]==-1:
                colors[i]=0
                if solve(i)==False:
                    return False
        return True
                