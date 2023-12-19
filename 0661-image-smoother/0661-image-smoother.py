class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = map(len,[img,img[0]])
        ans = deepcopy(img)
        for i in range(m):
            for j in range(n):
                c = 0
                v = 0
                for I in range(i-1,i+2):
                    for J in range(j-1,j+2):
                        if 0<=I<m and 0<=J<n:
                            c+=1
                            v += img[I][J]
                ans[i][j] = floor(v/c)
        return ans
                
                            
                        