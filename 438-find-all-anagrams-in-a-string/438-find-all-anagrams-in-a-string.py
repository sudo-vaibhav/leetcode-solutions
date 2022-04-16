class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        k,n = len(s1),len(s2)
        if k>n: return []
        ct1,ct2 = defaultdict(int),defaultdict(int)
        for i in s1: ct1[i]+=1
        i = 0
        ans = []
        while i<n:
            cur = s2[i]
            ct2[cur]+=1
            if i>=k:
                ct2[s2[i-k]]-=1
                if ct2[s2[i-k]]==0:
                    del ct2[s2[i-k]]
            if ct1==ct2:
                ans.append(i-k+1)
            i+=1
            
        return ans
            