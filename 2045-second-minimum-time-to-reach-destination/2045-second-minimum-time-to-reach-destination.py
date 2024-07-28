class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        t1 = [inf]*n
        t2 = [inf]*n
        t1[0] = 0
        
        q = deque([(0,1)])
        while q:
            cur,temp = q.popleft()
            t = t1[cur] if temp==1 else t2[cur]
            if (t//change)%2==0:
                ttr = t+time
            else:
                ttr = (change-(t%change))+time+t
            for v in adj[cur]:
                if t1[v]==inf:
                    t1[v]=ttr
                    q.append((v,1))
                elif t2[v]==inf and t1[v]!=ttr:
                    # if v==n-1:
                    #     return ttr
                    t2[v]=ttr
                    q.append((v,2))
                # oldVal=d2[v]
                # d2[v],d1[v] = d1[v],ttr
                # if oldVal!=d2[v]:
                #     infc-=1
                # heappush(q,(ttr,v))
        return t2[n-1]
                    
                    
                