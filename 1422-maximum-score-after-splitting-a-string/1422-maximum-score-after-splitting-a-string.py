class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n-1):
            zc,oc = 0,0
            for j in range(i+1):
                if s[j]=="0":
                    zc+=1
            for j in range(i+1,n):
                if s[j]=="1":
                    oc+=1
            ans = max(ans,oc+zc)
        
        return ans