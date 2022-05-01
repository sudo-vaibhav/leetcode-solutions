class Solution:
    def reorganizeString(self, s: str) -> str:
        ct = Counter(s)
        ans = ""
        maxH = [(-ct[i],i) for i in ct]
        heapify(maxH)
        prev = None
        while maxH:
            cnt,cur = heappop(maxH)
            cnt *= -1
            cnt-=1
            if prev!=None and prev[0]!=0:
                heappush(maxH,prev)
            prev = (-cnt,cur)
            ans += cur
        
        return "" if len(ans)<len(s) else ans