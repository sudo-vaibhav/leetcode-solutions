class Solution:
    def frequencySort(self, s: str) -> str:
        ct = Counter(s)
        
        mh = []
        for k in ct:
            heappush(mh,(-ct[k],k))
        
        ans = []
        while mh:
            count,val = heappop(mh)
            ans = [*ans,*([val]*(-count))]
        return "".join(ans)