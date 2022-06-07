class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        class UF:
            def __init__(self):
                self.parent = {}
                self.sz=0
                # self.size = [1 for i in range(n)]
                # self.sz = n
            
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                else:
                    self.parent[pu]=pv
                    self.sz-=1
                    return True
            
            def find(self,v):
                if v not in self.parent:
                    self.parent[v]=v
                    self.sz+=1
                if self.parent[v]==v:
                    return v
                else:
                    self.parent[v] = self.find(self.parent[v])
                    return self.parent[v]
        
        uf = UF()
        land,water = 1,0
        arr = [[water for _ in range(n)] for _ in range(m)]
        moves = [0,1,0,-1,0]
        ans = []
        for i,j in positions:
            arr[i][j]=land
            uf.find((i,j))
            for di,dj in zip(moves[1:],moves[:-1]):
                I,J = di+i,j+dj
                if 0<=I<m and 0<=J<n and arr[I][J]==land:
                    uf.union((I,J),(i,j))
            ans.append(uf.sz)
            
        return ans
            