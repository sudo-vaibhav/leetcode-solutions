class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        
        @lru_cache(1000)
        def solve(i=0,used=0):
            if i==n:
                return 0
            cur = arr[i]
            canTakeCurrent=True
            ifTaken=used
            
            for c in cur:
                if 1<<(ord(c)-ord("a"))&used:
                    canTakeCurrent=False;break;
                ifTaken |= 1<<(ord(c)-ord("a"))
            ans = solve(i+1,used)
            if canTakeCurrent and len(Counter(cur))==len(cur):
                ans = max(ans,len(cur)+solve(i+1,ifTaken))
            return ans
        
        return solve()