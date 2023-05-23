class KthLargest:
    def addop(self,num):
        heappush(self.uh,num)
        if len(self.uh)==self.k:
            if self.lh and -self.lh[0]>self.uh[0]:
                val = heappop(self.uh)
                heappush(self.uh,-heappop(self.lh))
                heappush(self.lh,-val)
        elif len(self.uh)==self.k+1:
            heappush(self.lh,-heappop(self.uh))
                
    def __init__(self, k: int, nums: List[int]):
        self.lh,self.uh = [],[]
        self.k = k
        for num in nums:
            self.addop(num)
           

    def add(self, val: int) -> int:
        
        self.addop(val)
        return self.uh[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)