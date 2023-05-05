class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        cur,ans = 0,0
        vowels = "aeiou"
        for idx,c in enumerate(s):
            cur+=(c in vowels)
            if idx>=k:
                cur-=(s[idx-k] in vowels)
            if cur>ans:
                ans = cur
        return ans