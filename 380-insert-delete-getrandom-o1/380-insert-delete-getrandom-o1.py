class RandomizedSet:

    def __init__(self):
        self.nums,self.indices = [],{}

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            curLen = len(self.nums)
            self.indices[val] = curLen
            self.nums.append(val)
            return True
        return False
            
        
        
    def remove(self, val: int) -> bool:
        if val in self.indices:
            curIndex = self.indices[val]
            lastIndex = len(self.nums)-1
            lastVal = self.nums[lastIndex]
            self.indices[lastVal]=curIndex
            # print(lastIndex,curIndex,val,self.nums,self.indices)
            self.nums[lastIndex],self.nums[curIndex] = val,lastVal
            del self.indices[val]
            self.nums.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()