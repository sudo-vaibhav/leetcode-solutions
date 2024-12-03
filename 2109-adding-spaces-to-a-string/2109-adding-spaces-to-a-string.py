class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.sort()
        spaces = spaces[::-1]
        ans = ""
        for i in range(len(s)):
            if spaces and spaces[-1]==i:
                spaces.pop()
                ans+=" "
            ans += s[i]
        return ans