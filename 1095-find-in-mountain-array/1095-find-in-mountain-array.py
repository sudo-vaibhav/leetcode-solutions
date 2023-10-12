# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        def findPivot():
            l,r = 1,n-2
            while l<r:
                m = (l+r)//2
                if mountain_arr.get(m)>mountain_arr.get(m+1):
                    r = m
                else:
                    l = m+1
            return l+1
        
        pivot = findPivot()
        # print(pivot)
        # return pivot
        def find(l,r,flip=False):
            ans = inf
            while l<=r:
                m = (l+r)//2
                if mountain_arr.get(m)>=target:
                    if mountain_arr.get(m)==target:
                        ans = m
                    if flip:
                        l=m+1
                    else:
                        r = m-1
                else:
                    if flip:
                        r=m-1
                    else:
                        l = m+1
                    
            return ans
        # return pivot
        l = find(0,pivot-1)
        # print(l,pivot)
        r = find(pivot,n-1,True)
        ans = min(l,r)
        return ans if ans!=inf else -1