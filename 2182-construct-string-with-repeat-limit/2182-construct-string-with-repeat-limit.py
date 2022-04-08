class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ct = Counter(s)
        # prev = ('-',0)
        q = [[-ord(k),ct[k]] for k in ct.keys()]
        
        heapify(q)
        ans = ""
        while q:
            # print(q)
            cur = heappop(q)
            x = min(repeatLimit,cur[1])
            ans+=chr(-cur[0])*x
            cur[1]-=x
            if cur[1]>0:
                if q:
                    nex = heappop(q)
                    # print("next",q)
                    ans += chr(-nex[0])
                    nex[1]-=1
                    if nex[1]:
                        heappush(q,nex)
                    heappush(q,cur)
                else:
                    break
        return ans