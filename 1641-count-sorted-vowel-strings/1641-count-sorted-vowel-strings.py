class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def solve(n,prev):
            if(n==0): return 1
            else:
                count = 0
                for c in ["a","e","i","o","u"]:
                    if c >= prev:
                        count += solve(n-1,c)
                return count
            
        return solve(n,"a")