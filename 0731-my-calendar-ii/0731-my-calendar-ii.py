class MyCalendarTwo:

    def __init__(self):
        self.intvls = []
        self.ovl = []
    def overlap(self,s1,e1,s2,e2):
        s = max(s1,s2)
        e = min(e1,e2)
        return (s,e) if s<e else False
    def book(self, start: int, end: int) -> bool:
        # print(start,end,self.ovl)
        for s,e in self.ovl:
            if self.overlap(start,end,s,e)!=False:
                return False
        # print("proceeding")
        for s,e in self.intvls:
            temp = self.overlap(start,end,s,e)
            if temp!=False:
                self.ovl.append(temp)
        self.intvls.append((start,end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)