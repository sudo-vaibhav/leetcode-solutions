class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        m = max(arr)
        return arr.index(m)