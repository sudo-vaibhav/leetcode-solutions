class CustomStack:
    def __init__(self, maxSize: int):
        self.st = [0]*maxSize
        self.adjustments = [0]*maxSize
        self.i = -1
        self.maxSize = maxSize
    def isFull(self):
        return self.i==self.maxSize-1
    def push(self, x: int) -> None:
        if self.isFull():
            return
        self.i+=1
        self.st[self.i] = x
    def isEmpty(self):
        return self.i==-1
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.st[self.i]+self.adjustments[self.i]
        self.i -= 1
        if self.i>=0:
            self.adjustments[self.i]+=self.adjustments[self.i+1]
        self.adjustments[self.i+1]=0
        return val
        
    def increment(self, k: int, val: int) -> None:
        if self.i>=0:
            self.adjustments[min(self.i,k-1)]+=val
        # end = self.i-k
        # if end>=0:
        #     self.adjustments[end]-=val
    


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)