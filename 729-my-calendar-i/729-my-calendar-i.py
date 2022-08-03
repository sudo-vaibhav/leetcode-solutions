from sortedcontainers import SortedSet
class MyCalendar:

    def __init__(self):
        self.ss = [] #SortedSet()        
    def book(self, start: int, end: int) -> bool:
        end-=1
        for s,e in self.ss:
            if (start<=s<=e<=end) or (s<=start<=end<=e): # full overlap
                return False
            if s<=start<=e or s<=end<=e: # partial overlap
                return False
        self.ss.append((start,end)) # no overlap, so add
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)