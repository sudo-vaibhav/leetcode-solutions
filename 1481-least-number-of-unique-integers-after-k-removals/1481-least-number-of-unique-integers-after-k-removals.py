class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ct = Counter(arr)
        
        mh = [(ct[k],k) for k in ct]
        heapify(mh)
        while k:
            cnt,num = heappop(mh)
            cnt-=1
            if cnt>0:
                heappush(mh,(cnt,num))
            k-=1
        return len(mh)
        