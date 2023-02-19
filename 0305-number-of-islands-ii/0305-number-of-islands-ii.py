class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ilndCnt = 0
        grid = [[0]*n for _ in range(m)]
        papa = {}
        def unite(c1,c2):
            nonlocal ilndCnt
            p1,p2 = find(c1),find(c2)
            if p1!=p2:
                papa[p1]=p2
                ilndCnt-=1
        def find(c):
            nonlocal ilndCnt
            if c not in papa:
                papa[c]=c
                ilndCnt+=1
            p = papa[c]
            if p!=c:
                papa[c] = find(p)
            return papa[c]
        moves = [[-1,0],[1,0],[0,1],[0,-1]]
        ans = []
        for r,c in positions:
            grid[r][c]=1
            find((r,c))
            for dr,dc in moves:
                R,C = r+dr,c+dc
                if 0<=R<m and 0<=C<n and grid[R][C]==1:
                    unite((r,c),(R,C))
            ans.append(ilndCnt)  
        return ans