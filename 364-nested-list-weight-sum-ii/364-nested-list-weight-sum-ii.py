# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nl: List[NestedInteger]) -> int:
        
        
#         currently => sum(num*depth)

#           now need => sum((max-depth+1)*num)

#           sum(max*num-depth*num+num)

#

        totalSum = 0
        maxDepth = 0
        def solve(l,d=1):
            nonlocal maxDepth,totalSum
            ans = 0
            for i in l:
                if i.isInteger():
                    totalSum += i.getInteger()
                    maxDepth = max(maxDepth,d)
                    ans += i.getInteger()*d
                else:
                    ans += solve(i.getList(),d+1)
            else:
                maxDepth = max(maxDepth,d-1)
            return ans
        
        temp = solve(nl)
        return (maxDepth+1)*totalSum - temp
