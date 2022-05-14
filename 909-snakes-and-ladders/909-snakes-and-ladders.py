class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        if len(board)==1: return 0
        
        vals = [0]
        for i in range(n):
            leftToRight = i%2==0
            for j in range(n):
                vals.append(board[~i][j if leftToRight else ~j])
        vis = set()
        q = deque()
        q.append(1)
        vis.add(1)
        ans = 0
        while q:
            qsize = len(q)
            for _ in range(qsize):
                cur = q.popleft()
                if cur==n**2 and vals[cur]==-1:
                    return ans
                for i in range(1,6+1):
                    newPos = i+cur
                    if newPos<=n**2:
                        if vals[newPos]!=-1:
                            newPos = vals[newPos]
                        if newPos not in vis:
                            vis.add(newPos)
                            q.append(newPos)
            ans+=1
        return -1