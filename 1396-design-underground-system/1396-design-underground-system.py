class UndergroundSystem:

    def __init__(self):
        self.tripDist = defaultdict(int)
        self.tripCount = defaultdict(int)
        self.travelling = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelling[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        old = self.travelling[id]
        self.tripDist[(old[0],stationName)]+=t-old[1]
        self.tripCount[(old[0],stationName)]+=1
        del self.travelling[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.tripDist[(startStation,endStation)]/self.tripCount[(startStation,endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)