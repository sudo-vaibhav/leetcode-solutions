class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        add = [(sum(x),i) for i,x in enumerate(points)]
        sub = [(x[0]-x[1],i) for i,x in enumerate(points)]
        ans = inf
        add.sort()
        sub.sort()
        n = len(points)
        for i in range(len(points)):
#           <variable name> removed
            maxSub = sub[-2][0] if i==sub[-1][1] else sub[-1][0]
            minSub = sub[1][0] if i==sub[0][1] else sub[0][0]
            maxAdd = add[-2][0] if i==add[-1][1] else add[-1][0]
            minAdd = add[1][0] if i==add[0][1] else add[0][0]
            temp = max(maxSub-minSub,maxAdd-minAdd)
            ans = min(ans,temp)
        return ans
#         two possibilities add[x]-add[y] or sub[x]-sub[y]
#         if add[x] is to be removed, and we still want 