class StringIterator:

    def __init__(self, cs: str):
        self.prev,self.prevC,self.i,self.s = None,0,0,cs

    def next(self) -> str:
        if not self.hasNext(): return " "
        if self.prevC:
            self.prevC-=1
            return self.prev
        else:
            temp = self.i
            
            while self.i<len(self.s):
                if self.s[self.i].isalpha():
                    if self.i==temp:
                        self.prev = self.s[self.i]
                    else:
                        break
                else:
                    self.prevC = self.prevC*10+int(self.s[self.i])
                self.i+=1
            
            self.prevC-=1
            return self.prev
        

    def hasNext(self) -> bool:
        return self.prevC or self.i<len(self.s)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()