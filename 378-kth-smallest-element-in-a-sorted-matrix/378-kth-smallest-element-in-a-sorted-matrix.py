class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r = -10**9,10**9
        # ans = None
        while l<=r:
            m = (l+r)//2
            temp = 0
            for row in matrix:
                temp += bisect_right(row,m)
            if temp>=k:
                ans = m
                r = m-1
            else:
                l = m+1
        return l