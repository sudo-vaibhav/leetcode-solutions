class Solution:

    def __init__(self, w: List[int]):
        self.tot = 0
        self.w = w
        self.arr = []
        prefix = 0
        for num in w:
            prefix+=num
            self.arr.append(prefix)
        self.tot = prefix
    def pickIndex(self) -> int:
        val = random.random()*self.tot
        n = bisect_right(self.arr,val)
        return n        
