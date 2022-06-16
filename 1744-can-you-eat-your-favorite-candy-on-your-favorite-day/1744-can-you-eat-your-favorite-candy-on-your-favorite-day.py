class Solution:
    def canEat(self, cc: List[int], queries: List[List[int]]) -> List[bool]:
        @cache
        def pSum(idx):
            if idx<0:
                return 0
            return cc[idx]+pSum(idx-1)
        ans = []
        for cType,favDay,dayCap in queries:
            daysBeforeFavDay = favDay
            # if daysBeforeFavDay==0: ans.append(True)
            # else:
#                 last day you used your full day cap
            candsBeforeFavCands = pSum(cType-1)+1-dayCap
            if pSum(cType)<favDay+1:
                ans.append(False)
                continue
            ans.append(dayCap*daysBeforeFavDay>=candsBeforeFavCands)
        return ans