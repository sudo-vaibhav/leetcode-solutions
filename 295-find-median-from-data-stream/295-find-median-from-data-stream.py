class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap,-num)
        
        if len(self.maxHeap)-len(self.minHeap)>1:
            heappush(self.minHeap,-heappop(self.maxHeap))
        
        if len(self.maxHeap)>0 and len(self.minHeap)>0:
            if -self.maxHeap[0]>self.minHeap[0]:
                v1 = -heappop(self.maxHeap)
                v2 = heappop(self.minHeap)
                
                heappush(self.maxHeap,-v2)
                heappush(self.minHeap,v1)
        

    def findMedian(self) -> float:
        if len(self.maxHeap)>len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0]+self.minHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()