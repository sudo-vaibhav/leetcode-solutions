class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k,n = len(s1),len(s2)
        if k>n: return False
        ct1,ct2 = defaultdict(int),defaultdict(int)
        for i in s1: ct1[i]+=1
        i = 0
        while i<n:
            cur = s2[i]
            ct2[cur]+=1
            if i>=k:
                ct2[s2[i-k]]-=1
                if ct2[s2[i-k]]==0:
                    del ct2[s2[i-k]]
            if ct1==ct2:return True
            i+=1
            
        return False
            
            