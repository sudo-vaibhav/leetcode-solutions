class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.r,self.c = 0,0
        self.totR = len(vec)
        self.vec = vec
        self.progress()
    def progress(self):
        while self.r<self.totR and self.c>=len(self.vec[self.r]):
            self.c = 0
            self.r = self.r+1
            
    def next(self) -> int:
        cur = self.vec[self.r][self.c]
        self.c+=1
        self.progress()
        return cur
            

    def hasNext(self) -> bool:
        return self.r<self.totR


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()