# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        m,n = binaryMatrix.dimensions()
        ans = inf
        for i in range(m):
            l,r = 0,n-1
            while l<=r:
                mid = (l+r)//2
                if binaryMatrix.get(i,mid)==1:
                    ans = min(ans,mid)
                    r = mid-1
                else:
                    l = mid+1
                
        if ans == inf: return -1
        return ans