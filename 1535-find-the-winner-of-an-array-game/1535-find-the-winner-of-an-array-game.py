class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k>n-1:
            return self.getWinner(arr,n-1)
        q = deque(arr)
        wc = defaultdict(int)
        while True:
            n1,n2 = q.popleft(),q.popleft()
            winner = max(n1,n2)
            loser = min(n1,n2)
            q.appendleft(winner)
            q.append(loser)
            wc[winner]+=1
            if wc[winner]==k:
                return winner
        # return max(arr)