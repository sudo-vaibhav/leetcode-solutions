class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        q = deque()
        ans = [[0]*n for _ in range(m)]
        seen = set()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                    seen.add((i,j))
        moves = [[-1,0],[1,0],[0,1],[0,-1]]
        while q:
            lenQ = len(q)
            
            for _ in range(lenQ):
                i,j = q.popleft()
                dist = ans[i][j]
                for di,dj in moves:
                    I,J = i+di,j+dj
                    
                    if 0<=I<m and 0<=J<n and (I,J) not in seen:
                        ans[I][J] = dist+1
                        seen.add((I,J))
                        q.append((I,J))
        return ans