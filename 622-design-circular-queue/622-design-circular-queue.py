class MyCircularQueue:

    def __init__(self, k: int):
        self.sz = 0
        self.arr = [None]*k
        self.cap = k
        self.front = -1
        self.back = -1
    
    def dbg(self,*args):
        pass
        # print(self.arr,"front:",self.front,"back:",self.back,args)
    def enQueue(self, value: int) -> bool:
        self.dbg("enque",value)
        if self.isFull():
            return False
        newIdx = (self.back+1)%self.cap
        self.arr[newIdx] = value
        self.back = newIdx
        self.sz+=1
        if self.sz==1:
            self.front = 0
        return True
    
    def deQueue(self) -> bool:
        self.dbg("deque")
        if self.isEmpty():
            return False
        self.arr[self.front] = None
        self.sz-=1
        if self.sz==0:
            self.back = -1
            self.front = -1
        else:
            self.front = (self.front+1)%self.cap
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        self.dbg("front")
        return self.arr[self.front]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        self.dbg("rear")
        return self.arr[self.back]
    
    def isEmpty(self) -> bool:
        return self.sz == 0    
    
    def isFull(self) -> bool:
        return self.sz == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()