class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        q = deque()
        q.append((0,0,mat[0][0]))
        m,n = len(mat),len(mat[0])
        ans = []
        deltas = [(1,0),(0,1)]
        rev = False
        while q:
            qsize = len(q)
            tempans = []
            for _ in range(qsize):
                i,j,val = q.popleft()
                tempans.append(val)
                for di,dj in deltas:
                    I = i+di
                    J = j+dj
                    if 0<=I<m and 0<=J<n and mat[I][J]!=inf:
                        q.append((I,J,mat[I][J]))
                        mat[I][J] = inf
            if rev:
                tempans[:] = tempans[::-1]
            rev = not rev
            ans.extend(tempans)
        return ans
                        
                        