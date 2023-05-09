class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])
        dir = 0
        
        i,j=0,0
        
        seen = set()
        ans = []
        def valid(i,j):
            if (i,j) in seen: return False
            if i<0 or i>=m or j<0 or j>=n: return False
            return True
        
        def getNext(i,j):
            nonlocal dir
            I,J = 0,0
            fI,fJ = 0,0
            if dir==0:
                I,J = i,j+1
                fI,fJ = i+1,j
            elif dir==1:
                I,J = i+1,j
                fI,fJ = i,j-1
            elif dir==2:
                I,J = i,j-1
                fI,fJ = i-1,j
            else:
                I,J = i-1,j
                fI,fJ = i,j+1
            
            if valid(I,J):
                return (I,J)
            else:
                dir = (dir+1)%4
                return (fI,fJ)
        
        while len(seen)!=m*n:
            seen.add((i,j))
            ans.append(mat[i][j])
            i,j = getNext(i,j)
        
        return ans