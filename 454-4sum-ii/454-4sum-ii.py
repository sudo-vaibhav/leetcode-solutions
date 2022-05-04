class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        ans = 0
        nums3.sort()
        nums4.sort()
          
        @cache
        def canGet(target):
            res = 0
            i,j = 0,n-1
            while 0<=i<n and 0<=j<n:
                tot = nums3[i]+nums4[j]
                if tot>target:
                    j-=1
                elif tot<target:
                    i+=1
                else:
                    L,R = 0,0
                    l,r = nums3[i],nums4[j]
                    while i<n and nums3[i]==l:
                        i+=1
                        L+=1
                    while j>=0 and nums4[j]==r:
                        j-=1
                        R+=1
                    res += L*R
            return res

        for i in range(n):
            for j in range(n):
                S = nums1[i]+nums2[j]
                ans += canGet(-S)
        return ans