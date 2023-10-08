class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = map(len,[nums1,nums2])
        @cache
        def solve(i,j,someTaken=False):
            if i==m or j==n: return 0 if someTaken else -inf
            ans=nums1[i]*nums2[j]+solve(i+1,j+1,True)
            ans=max(ans,solve(i+1,j+1,someTaken),solve(i+1,j,someTaken),solve(i,j+1,someTaken))
            
            # for pairIdx in range(j,n):
            #     ans = max(ans,nums1[i]*nums2[pairIdx]+solve(i+1,pairIdx+1,True))
            return ans
        return solve(0,0)