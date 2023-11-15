class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.k = size
        self.r = 0
    def next(self, val: int) -> float:
        self.q.append(val)
        self.r += val
        if len(self.q)>self.k:
            self.r -= self.q.popleft()
        return self.r/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)