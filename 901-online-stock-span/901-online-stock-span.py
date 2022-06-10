class StockSpanner:

    def __init__(self):
        self.st = deque()       
        self.cnt = 1
    def next(self, price: int) -> int:
        while self.st and self.st[-1][0]<=price:
            self.st.pop()
        prev = self.st[-1][1] if self.st else 0
        ans = self.cnt-prev
        self.st.append((price,self.cnt))
        self.cnt+=1
        return ans