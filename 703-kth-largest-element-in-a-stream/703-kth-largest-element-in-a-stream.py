class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for num in nums:
            heappush(self.heap,num)
            if len(self.heap)>k:
                heappop(self.heap)
        self.k = k

    def add(self, num: int) -> int:
        heappush(self.heap,num)
        if len(self.heap)>self.k:
            heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)