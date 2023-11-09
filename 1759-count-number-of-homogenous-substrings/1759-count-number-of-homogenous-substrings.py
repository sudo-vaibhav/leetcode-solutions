class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = 0
        ans = 0
        MOD = 10**9+7
        for i,c in enumerate(s):
            prev+=1
            if i==len(s)-1 or c!=s[i+1]:
                ans = (ans+(prev*(prev+1))//2)%MOD
                prev=0
        return ans