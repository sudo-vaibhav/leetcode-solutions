class NumArray:

        

        
    def __init__(self, nums: List[int]):
        self.nums = [0]*len(nums)
        self.ftree = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.update(i,nums[i])

    def update(self,i,val):
        delta = val-self.nums[i]
        self.nums[i]=val;
        i+=1
        
        while i<=len(self.nums):
            self.ftree[i]+=delta;
            i+= i&(-i)    

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right)-self.getSum(left-1)

    def getSum(self,i):
        i+=1
        ans = 0
        while i>0:
            ans+= self.ftree[i]
            i-=i&(-i)
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)