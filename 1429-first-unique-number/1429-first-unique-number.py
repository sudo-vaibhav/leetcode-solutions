class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.ct = defaultdict(int)
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.q and self.ct[self.q[0]]>1:
            self.q.popleft()
        if self.q:
            return self.q[0]
        return -1

    def add(self, v: int) -> None:
        self.q.append(v)
        self.ct[v]+=1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)