class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i,j = 0,len(tokens)-1
        ans = 0
        cur = 0
        while i<=j:
            
            if tokens[i]<=power:
                power-=tokens[i]
                i+=1
                cur+=1
            elif cur>0:
                cur-=1
                power+=tokens[j]
                j-=1
                
            else:
                break
            ans = max(ans,cur)
        return ans