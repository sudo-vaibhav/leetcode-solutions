class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        p = {
            "a" : 0,
            "e" : 1,
            "i" : 2,
            "o": 3,
            "u": 4
        }
        cur = 0
        mi = {
          0: -1   
        }
        ans = 0
        for idx,c in enumerate(s):
            if c in p.keys():
                cur ^= 1<<p[c]
            if cur in mi:
                ans = max(ans,idx-mi[cur])
            else:
                mi[cur]=idx
        return ans