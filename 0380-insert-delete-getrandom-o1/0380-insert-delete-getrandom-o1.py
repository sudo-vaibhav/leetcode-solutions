class RandomizedSet:

    def __init__(self):
        self.loc = {}
        self.arr = []
    def insert(self, val: int) -> bool:
        if val not in self.loc:
            self.arr.append(val)
            self.loc[val] = len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        # print(self.arr,self.loc)
        if val in self.loc:
            loc = self.loc[val]
            if loc==len(self.arr)-1:
                pass
                # self.arr.pop()
            else:
                self.arr[loc],self.arr[len(self.arr)-1]=self.arr[-1],self.arr[loc]
                self.loc[self.arr[loc]]=loc
            del self.loc[val]
                
            
            self.arr.pop()
            
            # print("on removal",self.arr,self.loc)
            # if loc!=self.loc[lastVal]:
            #     self.loc[lastVal]=loc
            return True
        return False

    def getRandom(self) -> int:
        return self.arr[randint(0,len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()