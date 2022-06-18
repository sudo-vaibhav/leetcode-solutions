class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i1,self.i2 = 0,0
        self.n1,self.n2 = len(v1),len(v2)
        self.v1,self.v2 = v1,v2
        self.v1Turn = True
    def next(self) -> int:
        vec = self.v1 if self.v1Turn else self.v2
        temp = None
        if self.v1Turn:
            if self.i1<self.n1:
                temp = self.v1[self.i1]
                self.i1+=1
            self.v1Turn = not self.v1Turn
            if temp==None:
                return self.next()
            else:
                return temp
        else:
            if self.i2<self.n2:
                temp = self.v2[self.i2]
                self.i2+=1
            self.v1Turn = not self.v1Turn
            if temp==None:
                return self.next()
            else:
                return temp
            
    def hasNext(self) -> bool:
        return self.i1<self.n1 or self.i2<self.n2

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())