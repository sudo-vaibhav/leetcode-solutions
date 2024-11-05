class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        # chunks = []
        for i in range(0,len(s),2):
            chunk = s[i:i+2]
            if chunk in "010":
                ans+=1
        return ans