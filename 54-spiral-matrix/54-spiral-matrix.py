class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nextDir = {
            "right":"down",
            "down":"left",
            "left":"up",
            "up":"right"
        }
        m,n = len(matrix),len(matrix[0])
        vis = set()
        ans = []
        i,j = 0,0
        dir = "right"
        while len(vis)!=m*n:
            ans.append(matrix[i][j])
            vis.add((i,j))
            if dir=="right":
                if j==n-1 or (i,j+1) in vis:
                    i+=1
                    dir = nextDir[dir]
                else:
                    j+=1
            elif dir=="down":
                if i==m-1 or (i+1,j) in vis:
                    j-=1
                    dir = nextDir[dir]
                else:
                    i+=1
            elif dir=="left":
                if j==0 or (i,j-1) in vis:
                    i-=1
                    dir = nextDir[dir]
                else:
                    j-=1
            else: # up
                if i==0 or (i-1,j) in vis:
                    j+=1
                    dir = nextDir[dir]
                else:
                    i-=1
                
        return ans
            