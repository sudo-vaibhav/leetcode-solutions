class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        m,n = map(len,[box,box[0]])
        
        newBox = [[0]*m for _ in range(n)]
        STONE,OBS,EMPTY="#*."
        for i in range(m):
            for j in range(n):
                newBox[j][m-1-i] = box[i][j]
        # print(newBox)
        for col in range(m):
            row = n-2
            while row>=0:
                if row!=n-1 and newBox[row+1][col]==EMPTY and newBox[row][col]==STONE:
                    newBox[row+1][col],newBox[row][col]=newBox[row][col],newBox[row+1][col]
                    row+=1
                else:
                    row-=1
        return newBox
                