class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        c = Counter(s)
        for g in "abc":
            if g not in c:
                c[g]=0
        if min(c.values())<k:
            return -1
        if k==0:
            return 0
        def combine(d1,d2):
            fin = {}
            for k in "abc":
                fin[k]=d1[k]+d2[k]
            return min(fin.values())
        def solve(s):
            rCount = deepcopy(c)
            # rCount[s[0]]-=1
            ans = len(s)
            r = 0
            # while r<len(s) and combine(defaultdict(int),rCount)>=k:
            #     ans = min(ans,len(s)-r)
            #     rCount[s[r]]-=1
            #     r+=1
            # ans = min(ans,len(s)-r)
            # print(rCount)
            lCount = defaultdict(int)
            for i in range(-1,len(s),1):
                if i>=0:
                    lCount[s[i]]+=1
                # while r<=i:
                #     rCount[s[r]]-=1
                #     r+=1
                while combine(lCount,rCount)>=k:
                    ans = min(ans,i+1+len(s)-r)
                    if r<len(s):
                        rCount[s[r]]-=1
                        r+=1
                    else:
                        break
                # ans = min(ans,i+1+len(s)-r)
                # print(lCount,rCount,i,r)
                # if combine(lCount,rCount)>=k:
                    
            return ans
                    
        return solve(s)