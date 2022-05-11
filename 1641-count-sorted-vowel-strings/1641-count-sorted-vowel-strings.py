class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["-","u","o","i","e","a"]
        characters = ["a","e","i","o","u"]
        @cache
        def solve(char,n):
            if n==1:
                return vowels.index(char)
            else:
                ans = 0
                for curChar in characters[characters.index(char):]:
                    ans += solve(curChar,n-1)
                return ans
        return solve("a",n)
            