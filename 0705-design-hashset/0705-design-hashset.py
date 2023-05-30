class MyHashSet:

    def __init__(self):
        self.M = 10_039
        self.arr = [[] for _ in range(0,self.M)]

    def add(self, key: int) -> None:
        m = key%self.M
        if key not in self.arr[m]:
            self.arr[m].append(key)

    def remove(self, key: int) -> None:
        m = key%self.M
        self.arr[m] = list(filter(lambda x:x!=key,self.arr[m]))

    def contains(self, key: int) -> bool:
        m =  key%self.M
        return key in self.arr[m]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)