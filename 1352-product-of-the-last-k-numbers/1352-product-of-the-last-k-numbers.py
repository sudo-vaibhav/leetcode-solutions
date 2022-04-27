class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        

    def add(self, num: int) -> None:
        if num==0:
            self.nums = []
        else:
            if self.nums==[]:
                self.nums.append(num)
            else:
                self.nums.append(self.nums[-1]*num)

    def getProduct(self, k: int) -> int:
        n = len(self.nums)
        if k==n: return self.nums[-1]
        if k>n:
            return 0
        return self.nums[n-1]//self.nums[n-k-1]        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)