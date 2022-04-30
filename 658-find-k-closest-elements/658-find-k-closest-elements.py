class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mh = []
        for elem in arr:
            heappush(mh,(-abs(elem-x),-elem))
            
            if len(mh)>k:
                heappop(mh)
        
        ans = []
        while mh:
            ans.append(-heappop(mh)[1])
        return sorted(ans)