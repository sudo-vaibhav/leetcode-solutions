class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
           
            time = {i+1:time[i] for i in range(0,n)}
            outDegree = defaultdict(int)
            inDegree = defaultdict(int)
            jda = defaultdict(list)
            
            for u,v in relations:
                inDegree[v]+=1
                outDegree[u]+=1
                jda[v].append(u)
             # need to account for disjoint graphs
#             def djikstra(i):
                
                
#                 return filter(lambda x:x!=-inf,dists.values())
            # q = deque()
            ans = -inf
            dists = defaultdict(lambda:-inf)
            hp = []
            for i in range(1,n+1):
                if outDegree[i]==0:
                    # q.append(i)
                    dists[i]=time[i]
            # dists[i]=time[i]
               
                    heappush(hp,[-dists[i],i])
            # print(dists)
            while hp:
                dist, node = heappop(hp)
                dist*=-1
                # if dist<jda
                for v in jda[node]:
                    if time[v]+dist>dists[v]:
                        dists[v]=time[v]+dist
                        heappush(hp,[-dists[v],v])  
                    # dists = djikstra(i)
                    # print(i,dists)
                    # ans = max(max(dists),ans)
            # print(dists)
            return max(dists.values())