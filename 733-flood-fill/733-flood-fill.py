class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        baseColor = image[sr][sc]
        if baseColor!=newColor:
            moves = [(-1,0),(1,0),(0,1),(0,-1)]
            def dfs(r,c):
                if 0<=r<m and 0<=c<n and image[r][c]==baseColor:
                    image[r][c]=newColor
                    for dr,dc in moves:
                        R,C = r+dr,c+dc
                        dfs(R,C)
            dfs(sr,sc)
        return image