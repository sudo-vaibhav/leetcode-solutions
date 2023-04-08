class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        temp = sorted(score,reverse=True)
        
        place = {s:i+1 for i,s in enumerate(temp)}
        ans = list(score)
        for idx,s in enumerate(score):
            if place[s]==1:
                ans[idx] = "Gold Medal"
            elif place[s]==2:
                ans[idx] = "Silver Medal"
            elif place[s]==3:
                ans[idx]="Bronze Medal"
            else:
                ans[idx]=str(place[s])
        return ans