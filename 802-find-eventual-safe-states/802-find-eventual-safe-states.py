class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        n = len(adj)
        WHITE,GREY,BLACK = range(3)
        color = [WHITE for i in range(n)]
        
        def dfs(node):
            if color[node]!=WHITE:
                return color[node] == BLACK
            
            # starting traversal so mark node grey
            color[node]=GREY
            
            for neig in adj[node]:
                if not dfs(neig):
                    return False
                    
            color[node]=BLACK
            return True
        
        ans = []
        for node in range(n):
            if dfs(node):
                ans.append(node)
        
        
        return ans