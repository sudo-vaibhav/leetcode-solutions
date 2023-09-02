class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n=len(s)
        dictionary = set(dictionary)
        @cache
        def solve(i):
            if i==n:
                return 0
            ans = 1+solve(i+1)
            temp = ""
            for j in range(i,n):
                temp+=s[j]
                if temp in dictionary:
                    ans = min(ans,solve(j+1))
            return ans
        
        return solve(0)