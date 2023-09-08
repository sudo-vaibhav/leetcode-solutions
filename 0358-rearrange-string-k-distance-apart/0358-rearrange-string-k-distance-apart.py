class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        ctr = list(map(list,Counter(s).items()))
        
        ans = ""
        
        while len(ans)<len(s):
            
            ref = len(ans)
            ctr.sort(key=lambda x:x[1],reverse=True)
            for i in range(len(ctr)):
                if ctr[i][1]>0:
                    temp = min(len(ans),k-1,26)
                    snippet = ans[-temp:] if temp>0 else ""
                    # print(snippet,ctr[i][1])
                    canUse = True
                    for c in snippet:
                        if c==ctr[i][0]:
                            canUse = False
                    if canUse:
                        ans+=ctr[i][0]
                        ctr[i][1]-=1
                        break
                    # break
            if len(ans)==ref:return ""
        # while len(ans)<len(s):
        #     print(blocked,heap,ans)
        #     if not heap: return ""
        #     ct,c = heappop(heap)
        #     ct *= -1
        #     ct-=1
        #     ans += c
        #     if ct!=0:
        #         blocked.append([-ct,c])
        #     if len(ans)>=k and blocked:
        #         heappush(heap,blocked.popleft())
        return ans