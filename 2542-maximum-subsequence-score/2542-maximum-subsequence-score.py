class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = list(zip(nums1,nums2))
        
        arr.sort(key=lambda x:-x[1])
        
        hp = []
        s = 0
        ans = 0
        for sNum,mNum in arr:
            if len(hp)==k:
                s-=heappop(hp)
            heappush(hp,sNum)
            s+=sNum
            if len(hp)==k:
                ans = max(ans,s*mNum)
        return ans