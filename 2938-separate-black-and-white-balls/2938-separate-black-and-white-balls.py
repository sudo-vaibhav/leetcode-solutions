class Solution:
    def minimumSteps(self, s: str) -> int:
        c = len(list(filter(lambda x:x=="1",s)))
        positions = list(range(len(s)-c,len(s)))
        actual = [i for i in range(len(s)) if s[i]=="1"]
        ans = sum([positions[i]-actual[i] for i in range(len(actual))])
        return ans