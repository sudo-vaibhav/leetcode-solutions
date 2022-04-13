class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = [[inf for i in range(n)] for j in range(n)]
        i,j=0,0
        ans[i][j]=1
        val = 1
        self.going = "right"
        moves = [[-1,0],[1,0],[0,1],[0,-1]]
        
        def checkDeadlock(i,j):
            for di,dj in moves:
                I,J = di+i,dj+j
                if I>=0 and I<n and J>=0 and J<n and ans[I][J]==inf:
                    return False
            # print("deadlock",i,j)
            return True
        
        def moveNext(i,j):
            # print(i,j)
            if checkDeadlock(i,j):return False
            
            if(self.going=="right"):
                if(j+1<n and ans[i][j+1]==inf):
                    return (i,j+1)
                else:
                    self.going="down"
                    return moveNext(i,j)
            if(self.going=="down"):
                if(i+1<n and ans[i+1][j]==inf):
                    return (i+1,j)
                else:
                    self.going="left"
                    return moveNext(i,j)
            if(self.going=="left"):
                if(j-1>=0 and ans[i][j-1]==inf):
                    return (i,j-1)
                else:
                    self.going="up"
                    return moveNext(i,j)
            if(self.going=="up"):
                if(i-1>=0 and ans[i-1][j]==inf):
                    return (i-1,j)
                else:
                    self.going="right"
                    return moveNext(i,j)
                    
            
        while(True):
            resp = moveNext(i,j)
            if resp==False:
                break
            else:
                i,j = resp
                ans[i][j]=val+1
                val+=1
              
        
        return ans