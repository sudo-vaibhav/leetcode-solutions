class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:
        left,top,right,down = [{} for _ in range(4)]
        colors = set()
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                colors.add(cur)
                if cur not in left:
                    left[cur] = j
                else:
                    left[cur] = min(left[cur],j)
                    
                if cur not in top:
                    top[cur] = i
                # else:
                #     top[cur] = min(top[cur])
                if cur not in right:
                    right[cur]=j
                else:
                    right[cur] = max(right[cur],j)
                    
                    
                if cur not in down:
                    down[cur]=i
                else:
                    down[cur]=i
        
        adj = {col:set() for col in colors}
        # for col in set()
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                for col in colors:
                    if col!=cur:
                        if left[col]>j or right[col]<j or top[col]>i or down[col]<i:
#                             no overlap
                            pass    
                        else:
                            adj[col].add(cur)
        
        vis = {}
        def topo(node):
            if node in vis:
                return vis[node]
            vis[node]=True
            for dest in adj[node]:
                temp = topo(dest)
                if temp:
                    return True
            vis[node]=False
        
        
        for col in colors:
            temp = topo(col)
            if temp:
                return False
        return True
                    