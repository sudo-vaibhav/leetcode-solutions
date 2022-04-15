class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        inWin = {}
        l,r = 0,0
        n = len(fruits)
        ans = 0
        while r<n:
            # print(inWin)
            cur = fruits[r]
            keys = inWin.keys()
            if len(keys)==2:
                if cur in keys:
                    inWin[cur]+=1
                else:
                    temp = fruits[l]
                    while l<n and len(inWin.keys())==2:
                        inWin[fruits[l]]-=1
                        if inWin[fruits[l]]==0:
                            del inWin[fruits[l]]
                        l+=1
                    inWin[cur] = 1
            else:
                if cur in keys:
                    inWin[cur] += 1
                else:
                    inWin[cur] = 1
            r+=1
            
            ans = max(ans,sum(inWin.values()))
                    
        return min(n,ans)
                