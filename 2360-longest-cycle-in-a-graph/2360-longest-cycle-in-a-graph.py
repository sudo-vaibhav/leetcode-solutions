class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -inf
        visited = set()
        
        def dfs(node,time=0,visiting={}):
            nonlocal ans
            if node==-1 or node in visited: return
            if node in visiting:
                ans = max(ans,time-visiting[node])
                return 
            visiting[node] = time
            dfs(edges[node],time+1,visiting)
            visited.add(node)
            del visiting[node]
            
        for i in range(n):
            if i not in visited:
                dfs(i)
              
        if ans == -inf:
            return -1
        return ans