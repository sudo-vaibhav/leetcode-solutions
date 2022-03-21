class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = collections.deque()
        q.append((sr,sc))
        orig = image[sr][sc]
        image[sr][sc] = newColor
        m,n = len(image),len(image[0])
        done = set()
        while q:
            r,c = q.popleft()
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                R,C = r+dr,c+dc
                # print(R,m,C,n)
                if (R>=0 and R<m and C>=0 and C<n):
                    if image[R][C] == orig:
                        image[R][C] = newColor
                        if (R,C) not in done:
                            q.append((R,C))
                            done.add((R,C))
                
                
        return image