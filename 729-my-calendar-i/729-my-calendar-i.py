from sortedcontainers import SortedSet
class MyCalendar:

    def __init__(self):
        self.ss = SortedSet()        

    def book(self, start: int, end: int) -> bool:
        end-=1
        for s,e in self.ss:
            if start<=s<=e<=end:
#                 full overlap
                return False
            if s<=start<=end<=e:
                return False
            if s<=start<=e or s<=end<=e:
                return False
        self.ss.add((start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)