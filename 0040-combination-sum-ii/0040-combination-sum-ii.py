class Solution:
    def combinationSum2(self, c: List[int], t: int) -> List[List[int]]:
        n = len(c)
        d = list(Counter(c).items())
        
        @cache
        def solve(i,newT):
            if i==len(d):
                return []
            cur,pos = d[i][0],d[i][1]
            ans = []
            for take in range(0,pos+1):
                temp2 = [cur]*take
                if take*cur<newT:
                    temp = solve(i+1,newT-take*cur)
                    for h in temp:
                        ans.append(temp2+h)
                elif take*cur==newT:
                    ans.append(list(temp2))
                    
            return ans
        return solve(0,t)