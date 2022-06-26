class TwoSum:

    def __init__(self):
        self.hmap = defaultdict(int)

    def add(self, number: int) -> None:
        self.hmap[number]+=1

    def find(self, value: int) -> bool:
        for key in self.hmap:
            self.hmap[key]-=1
            if value-key in self.hmap and self.hmap[value-key]>0:
                self.hmap[key]+=1
                return True
            self.hmap[key]+=1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)