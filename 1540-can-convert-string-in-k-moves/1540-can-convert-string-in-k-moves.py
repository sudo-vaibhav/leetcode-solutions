class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        diffs = defaultdict(int)
        n = len(s)
        m = len(t)
        if n!=m:
            return False
        
        for i in range(n):
            c1,c2 = s[i],t[i]
            
            if c1>c2:
                diffs[ord("z")-ord(c1)+1+ord(c2)-ord("a")]+=1
            elif c2>c1:
                diffs[ord(c2)-ord(c1)]+=1
        # print(diffs)
        diffKeys = list(sorted(list(diffs.keys())))
        used = {}
        for key in diffKeys:
            numberOfCandidates = diffs[key]
            while numberOfCandidates:
                toUse = key
                if toUse not in used:
                    used[toUse]=toUse
                else:
                    used[toUse]+=26
                if used[toUse] > k:
                    return False
                numberOfCandidates-=1
        
        return True