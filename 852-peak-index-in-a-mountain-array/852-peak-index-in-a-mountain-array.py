# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         m = max(arr)
#         return arr.index(m)

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l,r = 0,n-1
        
        while l<=r:
            m = l+(r-l)//2
            # print(l,r,m)
            if arr[m-1]<arr[m]>arr[m+1]:
                return m
            if arr[m]<arr[m+1]:
                l = m+1
            if arr[m]>arr[m+1]:
                r = m-1
        # print("\n")
    