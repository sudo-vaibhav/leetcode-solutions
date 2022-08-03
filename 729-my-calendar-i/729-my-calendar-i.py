from sortedcontainers import SortedList
class MyCalendar:
    def __init__(self):
        self.ss = SortedList()
        
    def overlap(self,i1,i2):
        begin,end = max(i1[0],i2[0]),min(i1[1],i2[1])
        return begin<end
    def book(self, start: int, end: int) -> bool:
        intvl = (start,end)
        pos = self.ss.bisect_left(intvl)
    
        if pos>0 and self.overlap(self.ss[pos-1],intvl):
            return False
        if pos<len(self.ss) and self.overlap(self.ss[pos],intvl):
            return False
    
        self.ss.add(intvl)
        return True