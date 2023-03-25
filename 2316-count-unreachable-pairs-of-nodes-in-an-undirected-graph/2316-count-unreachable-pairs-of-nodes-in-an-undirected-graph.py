class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        class UF:
            def __init__(self, V):
                self.parent = [i for i in range(V)]
                self.rank = [1]*V

            def union(self, u, v):
                pu, pv = self.find(u), self.find(v)
                if pu == pv:
                    return
                ru, rv = self.rank[pu], self.rank[pv]
                if ru < rv:
                    pu, pv = pv, pu
                    ru, rv = rv, ru
                self.parent[pv] = pu
                # if ru == rv:
                self.rank[pu] += self.rank[pv]

            def find(self, u):
                if self.parent[u] == u:
                    return u
                self.parent[u] = self.find(self.parent[u])
                return self.parent[u]
        uf = UF(n)
        
        for u,v in edges:
            uf.union(u,v)
        # for i in range(n):
        #     uf.find(i)
        ent = list(set([uf.find(i) for i in range(n)]))
        temp = [(i,uf.rank[uf.find(i)]) for i in ent]
        ans =0
        # print(temp)
        for i in range(n):
            ans += n-uf.rank[uf.find(i)]
        return ans//2