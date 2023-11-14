class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for i in c:
            if c[i]>=3:
                ans += 1
        seen = defaultdict(int)
        alphas = [chr(i) for i in range(ord("a"),ord("z")+1)]
        covered = set()
        for i in range(len(s)):
            seen[s[i]]+=1
            for char in alphas:
                if char != s[i] and seen[char] and c[char]-seen[char]>0:
                    covered.add(char+s[i]+char)
        
        return ans+len(covered)