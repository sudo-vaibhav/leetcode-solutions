class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # def solve(end):
        #     if end==0:return 1
        #     temp = solve(end-1)
        #     edge = end-temp-1
        #     if edge>=0:
        #         if s[edge]==s[end]: return temp+2
        #         else: return 1
        #     else:return 1
        # return max(solve(i) for i in range(n))
        @lru_cache(maxsize=10000)
        def isPalin(i,j):
            if i>=j:
                return True
            return s[i]==s[j] and isPalin(i+1,j-1)
        ans = 1
        result = [0,0]
        for end in range(n):
            for start in range(end):
                if isPalin(start,end):
                    if end-start+1>ans:
                        ans = end-start+1
                        result = (start,end)
        return s[result[0]:result[1]+1]