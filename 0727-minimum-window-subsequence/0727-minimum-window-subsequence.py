class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        @cache
        def dfs(curIdx, doneTill):
            if doneTill == len(s2):
                return curIdx

            ind = s1.find(s2[doneTill], curIdx + 1)
            return float("inf") if ind == -1 else dfs(ind, doneTill + 1)

        ansLen, ans = inf, ""
        for idx, curChar in enumerate(s1):
            if curChar == s2[0]:
                endIdx = dfs(idx, 1)
                if endIdx - idx < ansLen:
                    ansLen, ans = endIdx - idx, s1[idx : endIdx + 1]
        return ans