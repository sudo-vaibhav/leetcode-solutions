class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m,n = len(mat),len(mat[0])
        ans = 0
        lc,rc= 0,0
        psum = deepcopy(mat)
        for i in range(m):
            for j in range(1,n):
                psum[i][j] += psum[i][j-1]
        ans = 0
        success = defaultdict(int)
        while rc<n:
            wsize = rc-lc+1
            def isPos(lc,rc,wsize):
                rowSums = []
                for row in range(m):
                    rowSums.append(psum[row][rc]-(psum[row][lc-1] if lc>=1 else 0))
                running = 0
                for x in range(m):
                    running += rowSums[x]
                    if x>=wsize-1:
                        if running<=threshold:
                            return True
                        running -= rowSums[x-wsize+1]
                return False
            if wsize<=m and isPos(lc,rc,wsize):
                ans = max(ans,wsize)
            else:
                lc+=1
            rc+=1
        return ans