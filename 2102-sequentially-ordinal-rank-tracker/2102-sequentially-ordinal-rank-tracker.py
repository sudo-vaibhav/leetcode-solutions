from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.l = SortedList()
        self.i = 0
    def add(self, name: str, score: int) -> None:
        self.l.add((-score,name))
        
    def get(self) -> str:
        temp = self.l[self.i]
        self.i+=1
        return temp[1]

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()