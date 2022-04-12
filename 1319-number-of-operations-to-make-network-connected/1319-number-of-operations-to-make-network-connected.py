class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for c in connections:
            adj[c[0]].append(c[1])
            adj[c[1]].append(c[0])
        visited = [False for i in range(n)]
        def dfs(comp,parent):
            extraWires = 0
            for neig in adj[comp]:
                if not visited[neig]:
                    visited[neig]=True
                    extraWires+=dfs(neig,comp)
                else:
                    if neig != parent: 
                        # all already visited computers contribute to additional wires except parent,
                        # link to parent is obviously important otherwise one would have never reached this computer
                        # and thus that can't be counted as extra
                        extraWires+=1
            return extraWires
                    
        connectedComponents = 0
        extraWires=0
        for comp in range(n):
            if not visited[comp]:
                visited[comp] = True
                extraWires+=dfs(comp,-1)//2 # divide by two as graph is undirected and reports extra wire value twice
                connectedComponents+=1
        if extraWires < connectedComponents-1:
            return -1
        else: return connectedComponents-1
        
        