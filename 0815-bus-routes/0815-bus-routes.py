class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:return 0
        routes = [set(route) for route in routes]
        
        adj = defaultdict(set)
        q = deque([])
        seen = set([])
        
        for idx,route in enumerate(routes):
            for r2Idx in range(idx):
                route2 = routes[r2Idx]
                if route.intersection(route2):
                    adj[idx].add(r2Idx)
                    adj[r2Idx].add(idx)
                
            if source in route:
                # adj[source]=adj[source].union(route.difference(set([source])))
                q.append(idx)
                seen.add(idx)
                
        # mapping = defaultdict(list)
        
        # print(adj)        
        steps = 0
        while q:
            lenQ = len(q)
            
            for _ in range(lenQ):
                
                cur = q.popleft()
                if target in routes[cur]:
                    return steps+1
                for rIdx in adj[cur]:
                    if rIdx not in seen:
                        seen.add(rIdx)
                        q.append(rIdx)
                        # adj[cur]=adj[cur].union(route.difference(set([cur])))
                # for v in adj[cur]:
                #     if v not in seen:
                #         seen.add(v)
                #         q.append(v)
                # del adj[cur]       
            steps += 1

        return -1
        