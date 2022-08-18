class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ctr = Counter(arr)
        
        hp = []
        n = len(arr)
        for k in ctr:
            heappush(hp,(-ctr[k],k))
        
        c = 0
        rm = 0
        while hp:
            c+=1
            rm += -heappop(hp)[0]
            if rm>=n//2:
                break
        
        return c