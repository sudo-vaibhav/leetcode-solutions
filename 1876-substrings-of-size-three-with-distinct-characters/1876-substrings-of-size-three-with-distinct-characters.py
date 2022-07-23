class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        i = 0
        taken = 0
        ans = 0
        cur = deque()
        while i<n:
            cur.append(s[i])
            
            if i>=2:
                if len(set(cur))==len(cur):
                    ans+=1
                cur.popleft()
            i+=1
        
        return ans