class PeekingIterator:
    def __init__(self, it):
        self.it = it
        self.buf = None
        

    def peek(self):
        if not self.buf:
            self.buf = self.it.next()    
        return self.buf
        

    def next(self):
        if not self.buf:
            self.buf = self.it.next()
        val = self.buf
        self.buf = None
        return val
        

    def hasNext(self):
        return self.buf!=None or self.it.hasNext()