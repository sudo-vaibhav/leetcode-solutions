class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(lambda x:(x>="a"and x<="z")or(x>="0"and x<="9"),list(s.lower())))
        # print(s)
        for i in range(len(s)):
            if s[i]!=s[-i-1] : return False
        else: return True