class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        ref = 0
        MOD = (10**9)+7
        n = len(nums1)
        sortedNums1 = sorted(nums1)
        for i in range(n):
            ref += abs(nums1[i]-nums2[i])
            # ref %= MOD
        if ref==0:
            return 0
        
        ans = ref
        for i in range(n):
            lb = bisect_left(sortedNums1,nums2[i])
            ub = bisect_right(sortedNums1,nums2[i])
            val = nums2[i]
            cur = abs(nums1[i]-nums2[i])
            if ub>0 and sortedNums1[ub-1]==nums2[i]:
                ans = min(ans,(ref-cur))
                continue
            if lb>0:
                ans = min(ans,ref - cur + abs(sortedNums1[lb-1]-val))
            if ub<n:
                ans = min(ans,ref - cur + abs(sortedNums1[ub]-val))
            # if ans
        return ans%MOD