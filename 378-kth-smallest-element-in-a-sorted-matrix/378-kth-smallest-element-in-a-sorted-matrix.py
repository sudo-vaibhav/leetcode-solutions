class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r = -10**9,10**9
        while l<=r:
            m = (l+r)//2
            temp = sum(bisect_right(row,m) for row in matrix)
            if temp>=k: r = m-1
            else: l = m+1
        return l