class MovingAverage:

    def __init__(self, size: int):
        self.nums = deque()
        self.n = size
        self.s = 0

    def next(self, val: int) -> float:
        self.s+=val
        self.nums.append(val)
        if len(self.nums)>self.n:
            self.s-=self.nums.popleft()
        return self.s/len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)