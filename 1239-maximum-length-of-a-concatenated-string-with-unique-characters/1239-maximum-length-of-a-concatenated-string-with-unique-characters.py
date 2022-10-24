class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        def solve(i=0,used=0):
            if i==n: return 0
            cur,canTakeCurrent = arr[i],True
            ans = solve(i+1,used)
            for c in cur:
                if 1<<(ord(c)-ord("a")) & used:break
                used |= 1<<(ord(c)-ord("a"))
            else: ans = max(ans,len(cur)+solve(i+1,used))
            return ans
        return solve()