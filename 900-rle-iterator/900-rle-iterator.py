class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.N = len(encoding)
        self.idx = 0
        self.nums = encoding

    def next(self, n: int) -> int:
        if self.idx>=self.N:
            return -1
        if self.nums[self.idx]>=n:
            self.nums[self.idx]-=n
            n=0
            return self.nums[self.idx+1]
        else:
            n-=self.nums[self.idx]
            self.nums[self.idx]=0
            self.idx+=2
            return self.next(n)
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)