class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = map(len,[nums1,nums2])

        @cache
        def solve(i,j):
            if i==m or j==n:return 0
            if nums1[i]==nums2[j]:
                return 1+solve(i+1,j+1)
            return max(solve(i+1,j),solve(i,j+1))
            
        return solve(0,0)