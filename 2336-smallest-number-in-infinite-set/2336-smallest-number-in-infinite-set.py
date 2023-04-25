from sortedcontainers import SortedSet
class SmallestInfiniteSet:

    def __init__(self):
        self.s = SortedSet()
        for i in range(1,1001):
            self.s.add(i)
     
    def popSmallest(self) -> int:
        ans=self.s[0]
        self.s.remove(
        ans)
        return ans
    def addBack(self, num: int) -> None:
        self.s.add(num)
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)