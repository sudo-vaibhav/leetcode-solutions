# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.g = self.gen(nestedList)
        
    def gen(self,nestedList):
        for l in nestedList:
            if l.isInteger():
                yield l.getInteger()
            else:
                yield from self.gen(l.getList())
                
    def next(self) -> int:
        
        return self.nex
    
    def hasNext(self) -> bool:
        try:
            self.nex = next(self.g)
            return True
        except:
            return False
        # if len(self.st)
#         lis,idx = self.st[-1]
#         if lis[idx].isInteger():
#         while len(self.st[-1][0]) and not self.st[-1][0][self.st[-1][1]].isInteger():
#             self.st.append((self.st[-1][0][self.st[-1][1]],0))
        
#         if len(self.st[-1][0]) and self.st[-1][0][self.st[-1][1]].isInteger():
#             return True
#         else:
            
        # while self.st and self.st[-1][1]==len(self.st[-1][0])-1:
        #     self.st.pop()
        # if self.st:
        #     self.st[-1][1]+=1
        # if self.st[-1][0]
        # try:
            # self.st[-1][0][self.st[-1][1]]
            # return True
        # except:
            # return False
    

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())