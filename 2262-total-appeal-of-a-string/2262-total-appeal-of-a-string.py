class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        
        last = {}
        prev = 0
        res = 0
        for i in range(n):
            cur = s[i]
            if cur in last:
                tempans = prev+i-last[cur]
            else:
                tempans = prev+i+1
            prev = tempans
            last[cur] = i
            res+= tempans
        
        return res