class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ct = Counter(nums)
        
        mh = []
        for k in ct:
            heappush(mh,(ct[k],-k))
        
        ans = []
        while mh:
            count,val = heappop(mh)
            ans = [*ans,*([-val]*count)]
        return ans