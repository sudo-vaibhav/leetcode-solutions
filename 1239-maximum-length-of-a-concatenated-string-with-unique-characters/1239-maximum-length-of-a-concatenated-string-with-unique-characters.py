class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        def solve(i=0,used=0):
            if i==n: return 0
            cur = arr[i]
            canTakeCurrent=True
            ifTaken=used
            ans = solve(i+1,used)
            for c in cur:
                if 1<<(ord(c)-ord("a")) & ifTaken: canTakeCurrent=False
                ifTaken |= 1<<(ord(c)-ord("a"))
            if canTakeCurrent:
                ans = max(ans,len(cur)+solve(i+1,ifTaken))
            return ans
        return solve()