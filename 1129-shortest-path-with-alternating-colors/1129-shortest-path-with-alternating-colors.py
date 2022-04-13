class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        d1 = [inf for i in range(n)]
        d1[0]=0
        d2 = list(d1)
        
        adj = [{0:[],1:[]} for i in range(n)]
        
        for e in redEdges:
            adj[e[0]][0].append(e[1])
        for e in blueEdges:
            adj[e[0]][1].append(e[1])            
        
        def bfs(node,prevColor,seen=set()):
            distances = [inf for i in range(n)]
            distances[0] = 0
            q = deque() 
            q.append((node,prevColor))
            q.append((node,1-prevColor))
            dist = 0
            while q:
                dist+=1
                qs = len(q)
                while qs:
                    qs-=1
                    cur = q.popleft()
                    if (cur in seen):continue
                    seen.add(cur)
                    curNode,curColor = cur
                    newColor = 1-curColor
                    for neig in adj[curNode][newColor]:
                        distances[neig] = min(dist,distances[neig])
                        q.append((neig,newColor))
            return distances



        d1 = bfs(0,0)
        # d2 = bfs(0,1)
        
        # print(adj,d1,d2,sep="\n")
        ans = [-1 for i in range(n)]
        for i in range(n):
            temp = min(d1[i],d2[i]) 
            if temp!=inf:
                ans[i] = temp 
        return ans