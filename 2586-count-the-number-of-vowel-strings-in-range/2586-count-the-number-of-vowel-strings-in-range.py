class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        for s in words[left:right+1]:
            t = s[0]+s[-1]
            if len(set(t).difference(set("aeiou")))==0:
                ans+=1
        return ans