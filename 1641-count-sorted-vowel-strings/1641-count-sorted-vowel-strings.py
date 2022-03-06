class Solution:
    
    def countVowelStrings(self, n: int) -> int:
        vowels = ("a","e","i","o","u")
        
        @cache
        def solve(n,prev):
            if(n==0): return 1
            else:
                count = 0
                for c in vowels:
                    if c >= prev:count += solve(n-1,c)
                return count
            
        return solve(n,"a")