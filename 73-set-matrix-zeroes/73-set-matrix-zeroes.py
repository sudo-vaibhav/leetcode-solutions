class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m,n = len(mat),len(mat[0])
        row0 = False
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    if i==0: 
                        row0 = True
                    else:
                        mat[i][0] = 0
                    mat[0][j] = 0
                    
        # print(row0,mat)
        
        for i in range(m-1,0,-1):
            for j in range(n-1,-1,-1):
                # if i==0 and row0:
                #     mat[0][j]=0
                # else:
                if mat[0][j]==0 or mat[i][0]==0:
                    mat[i][j]=0
        if row0:
            for j in range(0,n):
                mat[0][j]=0
        
        