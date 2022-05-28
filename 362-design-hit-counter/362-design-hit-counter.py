class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        ub = timestamp
        lb = timestamp-300
        
        ir = bisect_right(self.hits, ub)
        il = bisect_right(self.hits,lb)
        
        return ir-il

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)