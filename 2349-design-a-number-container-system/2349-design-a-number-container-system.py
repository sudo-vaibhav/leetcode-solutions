from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.itov = {}
        self.vtoi = {}

    def change(self, index: int, number: int) -> None:
        if index in self.itov:
            oldVal = self.itov[index]
            self.vtoi[oldVal].remove(index)
        self.itov[index] = number
        if number not in self.vtoi:
            self.vtoi[number] = SortedSet()
            
        self.vtoi[number].add(index)
    def find(self, number: int) -> int:
        if number not in self.vtoi or len(self.vtoi[number])==0:
            return -1
        return self.vtoi[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)