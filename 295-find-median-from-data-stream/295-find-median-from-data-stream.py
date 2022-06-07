class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap,-num)
        heappush(self.minHeap,-heappop(self.maxHeap))
        
        if len(self.minHeap)>len(self.maxHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap)!=len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0]+self.minHeap[0])/2