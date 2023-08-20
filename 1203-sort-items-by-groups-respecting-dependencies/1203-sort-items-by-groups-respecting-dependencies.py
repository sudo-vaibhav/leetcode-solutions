class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        misc_group_ids = m
        for i in range(n):
            if group[i]==-1:
                group[i]=misc_group_ids
                misc_group_ids += 1
        
        ig = defaultdict(list)
        ideg = defaultdict(int)
        
        gg = defaultdict(list)
        gdeg = defaultdict(int)
        def topo(graph,ideg,n):
            q = deque()
            # seen = set()
            for i in range(n):
                if ideg[i]==0:
                    q.append(i)
                    # seen.add(i)
            ans = list(q)  
            # print(ans)
            while q:
                lenQ = len(q)
                for _ in range(lenQ):
                    cur = q.popleft()
                    for v in graph[cur]:
                        ideg[v]-=1
                        if ideg[v]==0:
                            ans.append(v)
                            q.append(v)
            if len(ans)<len(ideg):
                return []
            return ans
                    
                
        for i in range(n):
            for prev in beforeItems[i]:
                ig[prev].append(i)
                ideg[i]+=1
                
                if group[i]!=group[prev]:
                    gg[group[prev]].append(group[i])
                    gdeg[group[i]]+=1
                    
        iorder = topo(ig,ideg,n)
        gorder = topo(gg,gdeg,misc_group_ids)
        # print(iorder,gorder)
        if not iorder or not gorder: return []
        og = defaultdict(list)
        for i in iorder:og[group[i]].append(i)
        ans = []
        for g in gorder:
            ans.extend(og[g])
        return ans