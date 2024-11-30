class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        ind = defaultdict(int)
        outd = defaultdict(int)
        adj = defaultdict(list)

        for u,v in pairs:
            ind[v]+=1
            outd[u]+=1
            adj[u].append(v)
            
        startNode = pairs[0][0]
        
        for k in outd:
            if outd[k]==ind[k]+1:
                startNode = k
                break
        # print(startNode)
        ans = []
        def visit(node):
            
            while adj[node]:
                visit(adj[node].pop())
            ans.append(node)
 
            # for v in adj[]
        visit(startNode)
        ans = ans[::-1]
        res = []
        for i in range(len(ans)-1):
            res.append((ans[i],ans[i+1]))
        return res