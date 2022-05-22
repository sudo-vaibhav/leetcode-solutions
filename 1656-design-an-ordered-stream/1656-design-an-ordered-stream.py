class OrderedStream:

    def __init__(self, n: int):
        self.chunks = [None]*n
        self.n = n
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        i = idKey-1
        self.chunks[i] = value
        ans = []
        while self.ptr < self.n:
            if self.chunks[self.ptr]==None:
                break
            else:
                ans.append(self.chunks[self.ptr])
                self.ptr+=1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)