class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(set)
        degree = {i:0 for i in range(1,n+1)}
        for pre,nex in relations:
            adj[pre].add(nex)
            degree[nex]+=1
        sems = 0
        while len(degree)>0:
            candidates = []
            for i in degree:
                if degree[i]==0:
                    candidates.append(i)
            if len(candidates)==0:
                return -1
            else:
                sems+=1
                for cand in candidates:
                    del degree[cand]
                    for dest in adj[cand]:
                        degree[dest]-=1
                    
        return sems
            