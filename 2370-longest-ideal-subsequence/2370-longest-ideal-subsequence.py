class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        d = defaultdict(int)
        
        for i in range(n-1,-1,-1):
            cur = s[i]
            temp = 0
            diff = ord(cur)-ord("a")
            for p in range(26):
                if abs(p-diff)<=k:
                    # print(chr(ord("a")+p),cur,i)
                    temp = max(temp,d[p]+1)
            d[diff]=max(temp,d[diff])
        return max(d.values())