class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def solve(i=0,used=0):
            if i==len(arr): return 0
            ans = solve(i+1,used)
            for c in arr[i]:
                if 1<<(ord(c)-ord("a")) & used: return ans
                used |= 1<<(ord(c)-ord("a"))
            return max(ans,len(arr[i])+solve(i+1,used))
        return solve()