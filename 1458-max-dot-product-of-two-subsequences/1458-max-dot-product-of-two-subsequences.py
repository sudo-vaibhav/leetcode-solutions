class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def solve(i,j,someTaken=False):
            if i==len(nums1) or j==len(nums2): return 0 if someTaken else -inf
            return max(
                nums1[i]*nums2[j]+solve(i+1,j+1,True),
                # solve(i+1,j+1,someTaken),
                solve(i+1,j,someTaken),
                solve(i,j+1,someTaken)
            )
        return solve(0,0)